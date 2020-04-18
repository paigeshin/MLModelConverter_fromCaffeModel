import coremltools

#p1 - caffemodel
#p2 - file that describes the architecture of the caffe model
caffe_model = ('oxford102.caffemodel', 'deploy.prototxt')

labels = 'flower-labels.txt'

coreml_model = coremltools.converters.caffe.convert(
    caffe_model,
    class_labels = labels,
    image_input_names = 'data'
)

coreml_model.save('FlowerClassifier.mlmodel')




