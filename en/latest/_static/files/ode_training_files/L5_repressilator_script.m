clc; clear; close all;
set(0,'DefaultFigureWindowStyle','docked')

% Tell Matlab which function to use, the time span, and the initial conditions
% Here, x = [mRNA ; protein ; mRNA ; protein ; mRNA ; protein]
[t, x] = ode45(@repressilator_function, [0 75], [0.1 0 0 0 0 0]);

% Plot the results
subplot(2,1,1); plot(t, x(:,1), 'b--', t, x(:,2), 'g');
subplot(2,1,2); plot(t, x(:,2), 'r--',t, x(:,4), 'b--', t, x(:,6), 'g');

% Add legends and axis labels to the plots
subplot(2,1,1)
legend('mRNA (mr)', 'protein (pr)')
xlabel('time (mins)')
ylabel('Repressor mRNA and protein levels')
subplot(2,1,2)
xlabel('time (mins)')
ylabel('Protein levels')

% ------------------------------------------------------------------------
% ODE Function
function dx = repressilator_function(t, x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is a function defining the relationships between the each repressor
% and their mRNAs
% Inputs:
%  - vector of time
%  - vector of x: [mRNA ; protein ; mRNA ; protein ; mRNA ; protein]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dx = zeros(6,1); % a column vector

% Define parameter values
alpha = 250; % sensitive parameter
beta = 5;
alpha0 = 0.0; % What happens if the basal expression is non-zero?
n = 10; % What happens if there is no cooperativity? n = 1

% Define the differential equations
dx(1) = alpha/(1+x(6)^n) + alpha0 - x(1);
dx(2) = -beta*(x(2) - x(1));
dx(3) = alpha/(1+x(2)^n) + alpha0 - x(3);
dx(4) = -beta*(x(4) - x(3));
dx(5) = alpha/(1+x(4)^n) + alpha0 - x(5);
dx(6) = -beta*(x(6) - x(5));

end