cd aind/aind2-rnn
source activate aind2
jupyter notebook --ip=0.0.0.0 --no-browser


http://54.194.55.220:8888/?token=cb229ade04681d7947a607dcb017cde08e11dff0e91442fc



Instructions

    Follow the Udacity instructions to launch an EC2 GPU instance with the udacity-aind2 AMI. All of the remaining instructions should be executed in the EC2 instance.
    Activate the new environment: source activate aind2

    source activate aind2

    Clone the dog-project GitHub repository, and navigate to the downloaded folder:

    git clone https://github.com/udacity/aind2-rnn

    cd aind2-rnn

    conda env create -f requirements/aind-rnn-windows.yml
    activate aind-rnn
    set KERAS_BACKEND=tensorflow
    python -c "from keras import backend"

    Start Jupyter:  jupyter notebook RNN_project.ipynb

