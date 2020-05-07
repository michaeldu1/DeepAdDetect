//wget https://storage.googleapis.com/ads-dataset/subfolder-{0..10}.zip 
wget https://storage.googleapis.com/ads-dataset/resnet_negative.zip
7za -y x "*.zip" -odata
rm -rf *.zip
