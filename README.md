# いぬねこhealth

![image](https://user-images.githubusercontent.com/84378453/214183503-51e06ca1-d253-49fc-8ac4-77c7a6120af5.png)


## Author

- <a href="https://github.com/aohana-AO">https://github.com/aohana-AO</a>
  - CRAD機能
  - バックエンド
  - フロント
  - デプロイ
- <a href="https://github.com/hiraku0203">https://github.com/hiraku0203</a>
  - BCS計算
  - 適性食事量計算
  - API処理
  - フロント



## Overview

- 一日に与える食事量をご飯のカロリー量から計算する適正食事量計算機能。
- 外観と触感で大まかな太り具合を5段階で判断するBCS計算機能。
- ペットの毎日の様子を写真付きで記録することのできる日記投稿機能。
- 犬と柴犬の写真をランダムで表示させるギャラリー。
- アカウント作成、ログイン機能。

以上等をまとめdjangoでwebアプリの形にしました。



## サイトURL

https://inunekohealth.up.railway.app/


## Requirement

#### base
-

### 
    

#### data

- [カロリー計算](http://www.hidamari-hosp.com/2019/08/24/1411/)
- [BCS](https://www.env.go.jp/nature/dobutsu/aigo/2_data/pamph/petfood_guide_1808/pdf/6.pdf)
- [サイト下地](http://gettemplate.com/)


### API

[犬表示](https://dog.ceo/)
[柴犬表示](https://shibe.online/)


## Description


#### Home

- 適正食事量とBCS判断へとべる
- ログインしていれば投稿したものが下に表示される

#### About

- ログインしていれば自分が投稿したものを見ることができる

#### 投稿

- タイトルと文で記録を残せる日記機能
- 写真ファイルを添付できる

#### 犬ギャラリー

- 犬
    - 犬の写真をランダムで表示する。たまに狐
- 柴犬
    - 柴犬の写真をランダムで表示する

#### login

- アカウントを作成している場合はここでログイン可能

#### sign up

- アカウントを作成する


## プログラムの規模



## 今後について




## Reference
- requirements.txtのpip書き出しについて https://note.nkmk.me/python-pip-install-requirements/

- Railwayを用いたHeroku以外でのdjangoデプロイ https://kikuichige.com/15689/#toc2

- django4.x系列デプロイ後のcsrf検証失敗について https://blog.aoirint.com/entry/2022/django_3_x_to_4_x_csrf_verification_failed/

- Railwayダッシュボード https://railway.app/dashboard

