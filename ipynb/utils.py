import jax.numpy as np
import jax
import numpy as onp
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('JAX SGD')

class Bootstrap:
    def __init__(self, seed=123):
        '''
        boostrap 1d array
        usage:
        xs = np.arange(100)
        bs = Bootstrap(seed=123)
        for idx in bs.bootstrap(xs, group_size=50, n_boots=10):
            print(xs[idx].mean())
        '''
        self.rng = onp.random.RandomState(seed)

    def bootstrap(self, xs, group_size=100, n_boots = 100):
        '''
        input:
            xs: 1d np.array
            group_size: number of values in each bootstrap iteration
            n_boots: how many bootstrap groups
        output:
            iterator: bootstrapped
        '''
        xs = onp.array(xs)
        total_size = xs.shape[0]
        logger.info('Total size for bootstrap: %i' %total_size)
        if group_size > total_size:
            raise ValueError('Group size > input array size')
    
        for i in range(n_boots):
            idx = self.rng.randint(0, total_size, group_size)
            yield idx


@jax.jit
def loss_function(params, x, y):
    '''
    Root mean square loss function:

    input:
        - params: a list [w, b] where w are the weights and b is the bias term
        - x: input data for training (np.array)
        - y: target data (np.array)
    
    return:
        - RMSE value (float)
    '''
    predict = x.dot(params[0]) + params[1]
    deviation = y - predict
    squared_deviation = deviation ** 2
    mean_squared_deviation = squared_deviation.mean()
    return np.sqrt(mean_squared_deviation)