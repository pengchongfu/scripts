#!/bin/zsh
# The script is used for uplaod bulk videos to media.thu-skyworks.org

function ergodic(){
	for file in ` ls $1 `
	do
		if [ -d $1"/"$file ]
		then
		ergodic $1"/"$file
		else
		curl -b cookie -F file=@$1"/"$file https://wheretopostfile.com >>out4.html
		fi
	done
}
INIT_PATH="/where/is/myfile"

#curl -L https://mydomainname.com > out1.html
#curl -L --form "login=myadmin&password=mypassword" https://mydomainname.com/login >out2.html
curl -L --dump-header head1.txt -c cookie -d "login=myadmin&password=mypassword" "https://mydomainname.com/login" > out2.html
curl -L -e "https://mydomainname.com/login" -b cookie https://wheretojump.com > out3.html


#for i in /where/is/myfile/*.mp4
#do
#curl -b cookie -F file=@$i https://wheretopostfile.com >out4.html
#done

ergodic $INIT_PATH