# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:48:30 2021

@author: Sagar
"""

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time

model = pyo.ConcreteModel()

model.delta = pyo.Var(range(1, 7), within=pyo.Binary)
delta = model.delta

model.C1 = pyo.Constraint(expr= delta[1]+delta[3]+delta[5]+delta[6] >= 1)
model.C2 = pyo.Constraint(expr= delta[1]+delta[3]+delta[4]+delta[5] >= 1)
model.C3 = pyo.Constraint(expr= delta[1]+delta[2]+delta[4]+delta[6] >= 1)
model.C4 = pyo.Constraint(expr= delta[1]+delta[2]+delta[5] >= 1)
model.C5 = pyo.Constraint(expr= delta[2]+delta[3]+delta[4]+delta[6] >= 1)

model.obj = pyo.Objective(expr= 80*delta[1] + 50*delta[2] + 70*delta[3] + 52*delta[4] + 60*delta[5] + 44*delta[6], sense=minimize)

begin = time.time()
opt = SolverFactory('cplex')
result = opt.solve(model)
time_req = time.time() - begin

for i in range(1, 7):
    print(f'delta[{i}]: {pyo.value(delta[i])}')
    
print('Minimum distance to be travelled is {}'.format(pyo.value(model.obj)))
print('Time Required: {}'.format(time_req))