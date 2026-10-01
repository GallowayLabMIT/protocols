clc; clear; close all;
set(0,'DefaultFigureWindowStyle','docked')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% We will use ode45 to solve constitutive function over the range of
% time [0 100] for the initial conditions where mRNA = 0.1
% and protein is 0 so the intial condition is [0.1 0]. 
%
% What are the units of time? We have chosen the unit to be minutes.
% Depending on the constants you use, you could choose another unit.
% Remember to make sure your dimensions match!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Tell MATLAB which function to use, the time span, and the initial
% conditions.
% ode45 syntax:  [t,x] = ode45(ODE function, tspan, x0)
[t, x] = ode45(@constitutive_function, [0 100], [0.1 0]);

% Plot the results
% x(:,1) = mRNA and x(:,2) = protein
plot(t, x(:,1), 'b--', t, x(:,2), 'g');

% Add legends and axis labels to the plot
legend('mRNA (m)', 'protein (p)')
xlabel('time (mins)')
ylabel('mRNA and protein levels')


% ------------------------------------------------------------------------
% ODE Function
function dx = constitutive_function(t, x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is a function defining the relationship between mRNA x(1)
% and protein x(2)
% input = vector of time and x
% x is a matrix  (2,1)  of mRNA production x(1)
% and protein production x(2)
% x = [mRNA;Protein]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dx = zeros(2,1); % a column vector that initializes dx with two place-holder zeros

% Define parameter values
% note: assign meaningful names to the variables that avoid standard MATLAB
% function like "mean"
alpha_m = 5; % mRNA generation rate, units [=] 1/min
beta_m = 0.1; % mRNA degradation rate, units [=] 1/min
alpha_p = 2; % protein generation rate, units [=] 1/min*mol
beta_p = 0.5; % protein degradation rate, units [=] 1/min*mol

% Define the differential equations
dx(1) = alpha_m - beta_m*x(1);  %mRNA rate of change
dx(2) = alpha_p*x(1) - beta_p*x(2); %protein rate of change

end

