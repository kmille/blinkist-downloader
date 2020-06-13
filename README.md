# blinkist-downloader
Download audio from blinkist.com and convert it to mp3

- uses your cookies out of the browser
- converts the m4a files to mp3 (requires ffmpeg)

```bash
(venv) kmille@linbox blinkest-downloader master % python downloader.py --url https://www.blinkist.com/en/nc/reader/how-to-be-an-antiracist-en
Downloaded: data/How to Be an Antiracist_1.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_1'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_1'.mp3
Executing rm 'data/How to Be an Antiracist_1'.m4a
Downloaded: data/How to Be an Antiracist_2.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_2'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_2'.mp3
Executing rm 'data/How to Be an Antiracist_2'.m4a
Downloaded: data/How to Be an Antiracist_3.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_3'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_3'.mp3
Executing rm 'data/How to Be an Antiracist_3'.m4a
Downloaded: data/How to Be an Antiracist_4.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_4'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_4'.mp3
Executing rm 'data/How to Be an Antiracist_4'.m4a
Downloaded: data/How to Be an Antiracist_5.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_5'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_5'.mp3
Executing rm 'data/How to Be an Antiracist_5'.m4a
Downloaded: data/How to Be an Antiracist_6.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_6'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_6'.mp3
Executing rm 'data/How to Be an Antiracist_6'.m4a
Downloaded: data/How to Be an Antiracist_7.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_7'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_7'.mp3
Executing rm 'data/How to Be an Antiracist_7'.m4a
Downloaded: data/How to Be an Antiracist_8.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_8'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_8'.mp3
Executing rm 'data/How to Be an Antiracist_8'.m4a
Downloaded: data/How to Be an Antiracist_9.m4a
Executing ffmpeg -v 5 -y -i 'data/How to Be an Antiracist_9'.m4a -acodec libmp3lame -ac 2 -ab 320k 'data/How to Be an Antiracist_9'.mp3
Executing rm 'data/How to Be an Antiracist_9'.m4a
(venv) kmille@linbox blinkest-downloader master %
(venv) kmille@linbox blinkest-downloader master %
(venv) kmille@linbox blinkest-downloader master % ./concatmp3.sh data/How\ to\ Be\ an\ Antiracist.mp3 data/How\ to\ Be\ an\ Antiracist_*
+ mp3wrap 'data/How to Be an Antiracist.mp3' 'data/How to Be an Antiracist_1.mp3' 'data/How to Be an Antiracist_2.mp3' 'data/How to Be an Antiracist_3.mp3' 'data/How to Be an Antiracist_4.mp3' 'data/How to Be an Antiracist_5.mp3' 'data/How to Be an Antiracist_6.mp3' 'data/How to Be an Antiracist_7.mp3' 'data/How to Be an Antiracist_8.mp3' 'data/How to Be an Antiracist_9.mp3'
Mp3Wrap Version 0.5 (2003/Jan/16). See README and COPYING for more!
Written and copyrights by Matteo Trotta - <matteo.trotta@lib.unimib.it>
THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY! USE AT YOUR OWN RISK!

  11 %  --> Wrapping data/How to Be an Antiracist_1.mp3 ... OK
  22 %  --> Wrapping data/How to Be an Antiracist_2.mp3 ... OK
  33 %  --> Wrapping data/How to Be an Antiracist_3.mp3 ... OK
  44 %  --> Wrapping data/How to Be an Antiracist_4.mp3 ... OK
  55 %  --> Wrapping data/How to Be an Antiracist_5.mp3 ... OK
  66 %  --> Wrapping data/How to Be an Antiracist_6.mp3 ... OK
  77 %  --> Wrapping data/How to Be an Antiracist_7.mp3 ... OK
  88 %  --> Wrapping data/How to Be an Antiracist_8.mp3 ... OK
  100 % --> Wrapping data/How to Be an Antiracist_9.mp3 ... OK

  Calculating CRC, please wait... OK

data/How to Be an Antiracist_MP3WRAP.mp3 has been created successfully!
Use mp3splt to dewrap file; download at http://mp3splt.sourceforge.net!
(venv) kmille@linbox blinkest-downloader master %
(venv) kmille@linbox blinkest-downloader master %
(venv) kmille@linbox blinkest-downloader master % ./slowmp3.sh data/How\ to\ Be\ an\ Antiracist_MP3WRAP.mp3 "How to be racist.mp3"
+ input_file='data/How to Be an Antiracist_MP3WRAP.mp3'
+ output_file='How to be racist.mp3'
+ sox 'data/How to Be an Antiracist_MP3WRAP.mp3' 'How to be racist.mp3' tempo 0.8
sox WARN mp3-util: MAD lost sync
(venv) kmille@linbox blinkest-downloader master % ls How\ to\ be\ racist.mp3
-rw-r--r-- 1 kmille users 28M Jun 13 09:43 'How to be racist.mp3'
```
