# いぬねこhealth

![image](https://user-images.githubusercontent.com/84378453/214183503-51e06ca1-d253-49fc-8ac4-77c7a6120af5.png)


# Author

- <a href="https://github.com/aohana-AO">https://github.com/aohana-AO</a>
  - CRAD機能
  - バックエンド
  - フロント
  - デプロイ
  - 進捗・タスク管理
- <a href="https://github.com/hiraku0203">https://github.com/hiraku0203</a>
  - BCS計算
  - 適性食事量計算
  - API処理
  - フロント



# Overview

- 一日に与える食事量をご飯のカロリー量から計算する適正食事量計算機能。
- 外観と触感で大まかな太り具合を5段階で判断するBCS計算機能。
- ペットの毎日の様子を写真付きで記録することのできるCRAD機能。
- 犬と柴犬の写真をランダムで表示させるギャラリー。
- アカウント作成、ログイン機能。

以上等をまとめdjangoでwebアプリの形にしました。



# サイトURL

https://inunekohealth.up.railway.app/


# Requirement

## base
- Python==3.9
- Django==4.1.4
- PyCharm
- visual studio code
- Windows10,11

## CRAD周り
- django-allauth==0.51.0
- django-widget-tweaks==1.4.12
- oauthlib==3.2.2

## デプロイ
- gunicorn==20.1.0
- whitenoise==6.2.0
- Railway

## API処理
- requests==2.28.1
- requests-oauthlib==1.3.1
- sqlparse==0.4.3

## フロント
- js
- jQuery
- BootStorap5.0
- FontAwesome

    
## data

- [カロリー計算](http://www.hidamari-hosp.com/2019/08/24/1411/)
- [BCS](https://www.env.go.jp/nature/dobutsu/aigo/2_data/pamph/petfood_guide_1808/pdf/6.pdf)
- [サイト下地](http://gettemplate.com/)
- [犬表示](https://dog.ceo/)
- [柴犬表示](https://shibe.online/)


# Description


## 適性食事量計算、BCS計算

### ・外観と触感で大まかな太り具合を5段階で判断するBCSを計算できる
### ・一日に与える食事量をご飯のカロリー量から計算する

![image](https://user-images.githubusercontent.com/84378453/214193415-59ec27fa-42e9-4cbb-b6b2-ace44fc93328.png)


![image](https://user-images.githubusercontent.com/84378453/214193478-995dcead-35f7-409e-9092-49c65866ac06.png)


![image](https://user-images.githubusercontent.com/84378453/214193489-ab1041ef-66c1-4fb8-9abf-52518bc4c294.png)









## CRAD機能
### ・ログイン、ログアウト、サインイン機能
![image](https://user-images.githubusercontent.com/84378453/214191796-dff2d262-6c99-4b82-9366-1b3e4393f62e.png)

### ・タイトルと文で記録を残せる日記機能
![image](https://user-images.githubusercontent.com/84378453/214192251-ec381ca5-5139-47db-9b09-fd5cb3297d22.png)


### ・ログイン時、投稿一覧をindex下部に表示
![image](https://user-images.githubusercontent.com/84378453/214192353-2303433d-9a81-4e0b-9455-4efef5381b13.png)


![image](https://user-images.githubusercontent.com/84378453/214192329-b9d5f95b-21e1-4082-bd54-012e0624eb71.png)


## 犬ギャラリー
### ・犬 (犬の写真をランダムで表示する。たまに狐)

![image](https://user-images.githubusercontent.com/84378453/214191587-fad063b8-0e45-43a8-ab01-9ef48efb2545.png)

    
   
### ・柴犬 (柴犬の写真をランダムで表示する)

![image](https://user-images.githubusercontent.com/84378453/214191653-e77c23d2-3c40-41f4-bacf-9e1a186a1988.png)




# プログラムの規模

![image](https://user-images.githubusercontent.com/84378453/214192644-b5cdc450-f97b-47b0-9f09-9cd09d39297f.png)


# 今後について




# Reference
- requirements.txtのpip書き出しについて https://note.nkmk.me/python-pip-install-requirements/

- Railwayを用いたHeroku以外でのdjangoデプロイ https://kikuichige.com/15689/#toc2

- django4.x系列デプロイ後のcsrf検証失敗について https://blog.aoirint.com/entry/2022/django_3_x_to_4_x_csrf_verification_failed/

- Railwayダッシュボード https://railway.app/dashboard

