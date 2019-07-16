Code guide：
 
Prepare data

1. Download MiniImagenet dataset from the Google Drive.

   Download Link: https://drive.google.com/open?id=1q9lrXjjFct8RkoBPk8Mbkn1H1mZNFn5U
   
2. Extract subfolders to './OICEFSL/filelists/miniImagenet/images'.

3. Run script "OICEFFSL/filelists/miniImagenet/DataPreprocessing.sh".

Train:

python ./train.py --dataset miniImagenet --model ResNet18 --method baseline --train_aug

Test:

python ./save_features.py --dataset miniImagenet --model ResNet18 --method baseline --train_aug

python ./test.py --dataset miniImagenet --model ResNet18 --method baseline --train_aug
