# 打包上传
tar zcvf ../app.tar.gz --exclude=.git/ --exclude=__pycache__/ --exclude=.idea/ --exclude=deploy.sh .
cd ../
rsync -e 'sshj -p 3026' -avr --exclude=.git /Users/shenjianrong/test/prj/thunder_cms/ shenjianrong@101.254.157.124:~/prj/thunder_cms/
ssh stage<< 'END'
    cd ~/prj/erp_order/
    tar zxvf app.tar.gz
END