import pandas as pd
import os

from keras_timeseries.library.plot_utils import plot_timeseries
from keras_timeseries.library.recurrent import StatelessLSTM

data_dir_path = './data'
model_dir_path = './models/monthly-milk-production'

dataframe = pd.read_csv(filepath_or_buffer=os.path.join(data_dir_path, 'monthly-milk-production-pounds-p.csv'), sep=',')

print(dataframe.head())

timeseries = dataframe.as_matrix(['MilkProduction']).T[0]

print(timeseries)

network = StatelessLSTM()

network.load_model(model_dir_path=model_dir_path)

predicted_list = []
actual_list = []
timesteps = 6
for i in range(timeseries.shape[0] - timesteps - 1):
    X = timeseries[i:i + timesteps].T
    predicted = network.predict(X)
    actual = timeseries[i + timesteps + 1]
    predicted_list.append(predicted)
    actual_list.append(actual)
    print('predicted: ' + str(predicted) + ' actual: ' + str(actual))

plot_timeseries(actual_list, predicted_list, StatelessLSTM.model_name)




