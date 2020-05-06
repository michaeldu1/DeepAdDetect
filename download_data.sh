subfolders = ['subfolder-0.zip', 'subfolder-1.zip', 'subfolder-2.zip', 'subfolder-3.zip', 'subfolder-4.zip', 'subfolder-5.zip', 'subfolder-6.zip', 'subfolder-7.zip', 'subfolder-8.zip', 'subfolder-9.zip', 'subfolder-10.zip']

wget https://storage.googleapis.com/ads-dataset/subfolder-{0..10}.zip 
7za -y x "*.zip" -odata
//wget https://storage.googleapis.com/ads-dataset/subfolder-0.zip
//7z x subfolder-0.zip -odata -y
