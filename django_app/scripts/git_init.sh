cd /home/git
git init
git config --global user.email "mohini4git@gmail.com"
git config --global user.name "mohinid"
git add git_init.sh
git commit -m "Commited Django Code"
#git remote add origin https://github.com/mohiniuops/django_knowledgehub.git
git push https://'mohiniuops':'{{ git_pass }}'@'github.com/mohiniuops/django_knowledgehub.git'
#git remote add origin https://github.com/mohiniuops/django_knowledgehub.git
#git push -u origin master
