clc; clear; close all;
set(0,'DefaultFigureWindowStyle','docked')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Now that we've solved the result for a single set of parameters, we
% are interested in examining how the steady state is impacted by
% parameters.

% We will create a matrix to store the steady state values and initialize
% with zeros.
SS = zeros(2,1);

for i = 1:5 % vary alpha_m from 1 to 5

% This format allows me to put the parameters into the solver and vary
% alpha_m

% alternate ode45 format with anonymous function syntax
[t, x] = ode45(@( t, x ) constitutive_function_param( t, x, i, 0.1, 2, 0.05 ), [0 100], [0.1 0] );

% Save steady state values of mRNA and Protein
SS(1,i) = x(end,1); % mRNA
SS(2,i) = x(end,2); % Protein

% Save mRNA and protein trajectories for each value of alpha_m
mRNA(:,i) = x(:,1);
protein(:,i) = x(:,2);

% Save values of alpha_m in a vector
alpha_m(1, i) = i;

end

% Save steady state values of mRNA and protein as individual vectors
mRNA_ss= SS(1,:);
Protein_ss=SS(2,:);



% Plot the SS mRNA and protein vs alpha_m
figure
plot(alpha_m, mRNA_ss,'b--',alpha_m, Protein_ss,'g');

% Add legends and axis labels to the plot
legend('mRNA (m)', 'protein (p)')
xlabel('alpha_m')
ylabel('mRNA and protein levels')




% Plot the mRNA vs time for varying alpha_m
figure
plot(t, mRNA(:,1),'b', t, mRNA(:,2),'g', t, mRNA(:,3),'y', t, mRNA(:,4),'r--',t, mRNA (:,5),'p');

% Add legends and axis labels to the plot
legend('alpha_m=1', 'alpha_m=2', 'alpha_m=3', 'alpha_m=4', 'alpha_m=5','location','best')
xlabel('time')
ylabel('mRNA levels')



% Plot the protein vs time for varying alpha_m
figure
plot(t, protein(:,1),'b', t, protein(:,2),'g', t, protein(:,3),'y', t, protein(:,4),'r--',t, protein (:,5),'p');

% Add legends and axis labels to the plot
legend('alpha_m=1', 'alpha_m=2', 'alpha_m=3', 'alpha_m=4', 'alpha_m=5','location','best')
xlabel('time')
ylabel('protein levels')





%-------------------------------------------------------------------------
% ODE Function
function dx = constitutive_function_param(t, x, alpha_m,beta_m, alpha_p,beta_p)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is a function defining the relationship between mRNA x(1)
% and protein x(2)
% Inputs:
%  - vector of time
%  - vector of x where x is a matrix (2,1) of mRNA x(1)
%    and protein production x(2)
%  - parameters alpha_m, beta_m, alpha_p, and beta_p

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dx = zeros(2,1); % a column vector that initializes dx with two place-holder zeros

% Define the differential equations
dx(1) = alpha_m - beta_m*x(1);  % mRNA rate of change
dx(2) = alpha_p*x(1) - beta_p*x(2); % protein rate of change

end