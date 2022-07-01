import zipfile
import gdown

# you can add https://drive.google.com/file/d/ in front of the following file_id and download them manually through web browser.
sppe_pretrain_weight = '1OPORTWB2cwd5YTVBX-NE8fsauZJWsrtW'
yolo_pretrain_weight = '1g8uJjK7EOlqrUCmjZTtCegwnNsBig6zn'
sppe_trained_weight = '1_BwtYySpX9uWDgdwqw0UEppyMYYv1gkJ'
yolo_trained_weight = '13zXkuZ4dNm3ZOwstr1sSWKOOzJ19XZpN'
demo_data = '1N0JjazqW6JmBheLrn6RoDTSRXSPp1t4K'
sample_training_data='15dR-vVCEsg2z7mEVzJOF9YDW6YioEU3N'
scipy_data = '1c6vJQbAm_TcGyTCr1ah-x_R-iIYmT9TM'

url = 'https://drive.google.com/uc?id='+ sppe_pretrain_weight
output = './models/sppe/duc_se.pth'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id='+ yolo_pretrain_weight
output = './train_yolo/darknet/darknet53.conv.74'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id='+ sppe_trained_weight
output = './train_sppe/exp/coco/demo/model_10.pkl'
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id='+ yolo_trained_weight
output = './train_yolo/darknet/backup/demo/yolov3-mice_final.weights'
gdown.download(url, output, quiet=False)
                                    
url = 'https://drive.google.com/uc?id='+ demo_data
output = './data/demo.mp4'
gdown.download(url, output, quiet=False)   

url = 'https://drive.google.com/uc?id='+ sample_training_data
output = './data/sample_annotated_data.zip'
gdown.download(url, output, quiet=False)
                                    
url = 'https://drive.google.com/uc?id='+ scipy_data
output = '../../UI/data/scipy.data'
gdown.download(url, output, quiet=False)

# The following command do an unzip operation. You can also unzip the files manually.
with zipfile.ZipFile('./data/sample_annotated_data.zip', 'r') as zip_ref:
    zip_ref.extractall('./data/sample_annotated_data/')
