from __future__ import division
import random
import math
from random_initial import random_int_list
import numpy as np
import time
from matplotlib import pyplot as plt
import function

# --- COST FUNCTION ------------------------------------------------------------+

# function we are attempting to optimize (minimize)



# --- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self, x0):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        for i in range(0, num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0[i])
            #print(self.position_i)

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i)
        #print(self.position_i)
        #print(self.err_i)
        file_name = open('initial_fitness1', 'a', encoding='utf-8')
        line = str(self.err_i) + "    "
        file_name.write(line)
        file_name.close()
        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            #print(self.pos_best_i)
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 2  # cognative constant
        c2 = 2  # social constant

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                #self.position_i[i] = bounds[i][1]-50
                #self.position_i[i] = (self.pos_best_i[i-1]+self.pos_best_i[i-2])/2
                #self.position_i[i]=bounds[i][1]-50
                self.position_i[i] = random.random()*bounds[i][1]
            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                #self.position_i[i] = (self.pos_best_i[i-1]+self.pos_best_i[i-2])/2
                #self.position_i[i] = bounds[i][0]+900
                self.position_i[i] = random.random()*bounds[i][0]
                #self.position_i[i]=bounds[i][0]


class PSO():
    def __init__(self, costFunc, x0, bounds, num_particles, maxiter, verbose=False):
        global num_dimensions  #30
        num_dimensions = len(x0[1])
        err_best_g = -1  # best error for group
        pos_best_g = []  # best position for group

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(x0[i]))
            #print(Particle(x0[i]))
        # begin optimization loop
        i = 0
        print(type(swarm[0]))
        p = swarm[0]
        print(p.position_i)

        err_best_g1 = []
        maxiter1 = []
        while i < maxiter:

            time_start = time.time()
            if verbose: print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')
            # cycle through particles in swarm and evaluate fitness
            for j in range(num_particles):
                swarm[j].evaluate(costFunc)
                #print(type(swarm[j]))   Particle类型
                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_i)
                    err_best_g = float(swarm[j].err_i)


            # cycle through swarm and update velocities and position
            for j in range(0, num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)

            i += 1
            maxiter1.append(i)
            err_best_g1.append(err_best_g)


            time_end = time.time()
        print('time cost', time_end - time_start, 's')

        # print final results
        #print(initial)
        print('\nFINAL SOLUTION:')
        #print(type(initial))
        print(f'   > {pos_best_g}')
        print(f'   > {err_best_g}\n')
        #print(err_best_g1)
        #print(maxiter1)
        plt.scatter(maxiter1, err_best_g1 )
        plt.show()

if __name__ == "__PSO__":
    main()

# --- RUN ----------------------------------------------------------------------+



#initial = random_int_list(-100, 100, 30)
#bounds = [(-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32), (-32, 32)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
#bounds = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
#bounds = [(-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500), (-500, 500)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
bounds = [(-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-100, 100)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
#bounds = [(-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600), (-600, 600)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
initial = []
for j in range(0, 50):
    initial.append(random_int_list(-5.12, 5.12, 30))
    #print(initial[j])
#initial = [5, 5]  # initial starting location [x1,x2...]
#bounds = [(-500, 500), (-500, 500)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(function.func4, initial, bounds, num_particles=50, maxiter=1000, verbose=True)

#12357111415

#4 需要调整边界
#6 差一点
#8 10 不行
# 12 需要调整参数
#13 有问题