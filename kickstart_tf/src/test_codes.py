#Basic skeleton of TensorFlow code :
ow

##Load the data


##Manipulate the data to create features.
##Code Sample


def input_fn(dataset):sw
   ...  # manipulate dataset, extracting feature names and the label
   return feature_dict, label


##Define the feature column
###Define three numeric feature columns.
population = tf.feature_column.numeric_column('population')
crime_rate = tf.feature_column.numeric_column('crime_rate')
median_education = tf.feature_column.numeric_column('median_education',
                    normalizer_fn='lambda x: x - global_education_mean')

dd