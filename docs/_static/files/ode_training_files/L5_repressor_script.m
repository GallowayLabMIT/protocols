clc; clear; close all;
set(0,'DefaultFigureWindowStyle','docked')

% Tell Matlab which function to use, the time span, and the initial conditions
% Here, x = [repressor mRNA ; repressor protein ; target mRNA ; target protein]
[t, x] = ode45(@repressor_function, [0 100], [0.1 0 10 0]);

% Plot the results
subplot(2,1,1); plot(t, x(:,1), 'b--', t, x(:,2), 'g');
subplot(2,1,2); plot(t, x(:,3), 'b--', t, x(:,4), 'g');

% Add legends and axis labels to the plots
subplot(2,1,1)
legend('mRNA (mr)', 'protein (pr)')
xlabel('time (mins)')
ylabel('Repressor mRNA and protein levels')
subplot(2,1,2)
legend('mRNA (mt)', 'protein (pt)')
xlabel('time (mins)')
ylabel('Target mRNA and protein levels')


% ------------------------------------------------------------------------
% ODE Function
function dx = repressor_function(t, x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is a function defining the relationships between the repressor and
% target protein
% Inputs:
%  - vector of time
%  - vector of x: [repressor mRNA ; repressor protein ; target mRNA ; target protein]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dx = zeros(4,1); % a column vector

% Define parameter values
alpha_m = 1;
beta_m = 0.1;
alpha_p = 2;
beta_p = 0.05;
alpha_m0 = 0.01;
n = 2;
K = 200;

% Define the differential equations
dx(1) = alpha_m - beta_m*x(1);
dx(2) = alpha_p*x(1) - beta_p*x(2);
dx(3) = alpha_m0 + alpha_m*(1/(1 +(x(2)/K)^n)) - beta_m*x(3);
dx(4) = alpha_p*x(3) - beta_p*x(4);

end