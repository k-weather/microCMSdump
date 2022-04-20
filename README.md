# microCMSdump

microCMSのコンテンツをjsonにdumpするだけです

##　使い方

環境変数として以下の2つを登録してください

| MICROCMS_API_KEY | X-MICROCMS-API-KEY |
| ---- | ---- |
| MICROCMS_URL | API用のurlの/api以前 |

MICROCMS_URLは基本的にhttps://{アカウント名}.microcms.ioとかになるはずです

あとはpythonで実行すればcontents.outputとしてjsonダンプされます

##　Markdownを吐き出したい

microCMSはいまのところ、Markdownで書いていてもHTMLで出力されます\
markdownifyというライブラリを利用するとHTML->Markdownとできます\
コメントアウトしている個所を外して自分のAPI設定に合わせて修正すれば.mdで出力します
