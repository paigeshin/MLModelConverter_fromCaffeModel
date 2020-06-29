# MLModelConverter_fromCaffeModel

<<<<<<< HEAD
# Dropbox Resource for mlModel

[Link](https://www.dropbox.com/home/swift/mlmodels/flowerclassifier)

=======
## ❗️참고로 mlmodel이나 caffeemodel은 파일이 너무 커서 git에 안올라감
>>>>>>> e686673b8dea78a482c06f6c1e02834681aeee08

# How to make `pre-trained model` to `ML model`

### Necessary files to make MLModel which will be used on App Development

- caffemodel (.caffemodel)
- file that describes the architecture of the caffe model (.deploy.prototxt)
- labels (.txt)

### Conversion Workflow

pre-trained model(.caffemodel) -> Model(.mlmodel) → xCode → Your App 

### What we are going to use

- Oxford 102 Flower Dataset

### Installing CoremlTools using Python PIP

[https://pypi.org/project/pip/](https://pypi.org/project/pip/)

- PIP - Python package manager

        ### 설치 ###
        sudo python get-pip.py #이게 안되면 아래 line을 실행 
        curl 'https://bootstrap.pypa.io/get-pip.py' > get-pip.py && sudo python get-pip.py
        
        ### 버전 확인 ### 
        pip -v
        
        ### 환경구축 ###
        sudo pip install virtualenv
        mkdir Environments
        cd Environments
        virtualenv --python=/usr/bin/python2.7 python27 #virtual env가 python 2.7로 돌아가게 만듬 
        #위에 것이 안되면 아래 코드로 작동
        virtualenv -p=/usr/bin/python2.7 python27
        
        ### 실행 ####
        source python27/bin/python
        #위에 것이 안되면
        ./python27/bin/python #이제 터미널이 python27 env으로 진행.
        #기본적으로 python 2.7을 이용하기 위해서 하는 방법이다.
        #python은 버전에 매우 민감하기 때문에 특정 모듈을 사용하고자 할 때 이렇게 버전을 바꿔갈 수 있음.
        
        #빠져나오기 
        deactivate 

- 내가 편할려고 bash_profile에 추가

        alias ML='cd /Users/grosso/Environments;source python27/bin/activate;'

- python 환경 2.7일 때

        #ML tool 설치
        pip install -U coremltools
        
        #설치 중 에러 발생
        sudo easy_install nose
        sudo easy_install tornado

### `CafeModel` to `MLModel`

[https://pypi.org/](https://pypi.org/)

- Caffe Model 을 Core ML 로 바꾸기

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

⇒ "반드시 실행하기 전에 " `cd /Users/grosso/Environments; source python27/bin/activate;` 를 실행해서 python 2.7 버전으로 맞춰줘야 한다.
