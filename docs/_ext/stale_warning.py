import sphinx.application
import docutils.transforms
import docutils.nodes

import datetime
from pathlib import Path

__version__ = '0.1.0'


class StaleTransform(docutils.transforms.Transform):
    """
    Parses the generated document
    """
    default_priority = 210 # early transformation

    def apply(self):
        # Get the current source name, and trim off everything up to the "docs" part
        source = Path(self.document.settings._source)

        try:
            final_part_idx = source.parts.index('docs')
            abs_parent = Path('').joinpath(*source.parts[:final_part_idx + 1])
            source_relpath_with_ext = source.relative_to(abs_parent)
            source_relpath = source_relpath_with_ext.with_name(source_relpath_with_ext.stem)

        except ValueError:
            self.document.reporter.warning(f'Unable to parse local path of document {source}')
            return
        
        if str(source_relpath) not in self.document.settings.env.git_last_updated:
            # Skip this file; it doesn't have a git date
            return
        
        last_updated = datetime.datetime.fromtimestamp(
            int(self.document.settings.env.git_last_updated[str(source_relpath)][0].decode())
        )

        # Skip if in exclude category
        for exclude_pattern in self.document.settings.env.config.stale_warning_exclude:
            if source_relpath.match(exclude_pattern):
                return

        # Skip if not stale (e.g. has been updated this year)
        if datetime.datetime.now().year == last_updated.year:
            return

        # Insert the stale warning node!
        stale_node = docutils.nodes.admonition()
        stale_node += docutils.nodes.title('', 'Stale warning')
        stale_node += docutils.nodes.paragraph('',
            'This protocol has not been updated this year! Last update was on ' +
            last_updated.strftime(r'%B %d, %Y') + '.')
        self.document.insert(0, stale_node)

def setup(app: sphinx.application.Sphinx):
    """Sphinx extension entry point"""
    # Require the sphinx_last_updated_by_git extension
    app.setup_extension('sphinx_last_updated_by_git')
    app.add_config_value('stale_warning_exclude', [], 'env')
    app.add_post_transform(StaleTransform)
    return {
        'version': __version__,
        'parallel_read_safe': True,
    }