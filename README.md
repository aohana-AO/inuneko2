
![logo (37)](https://user-images.githubusercontent.com/84378453/214289507-a12aa13a-380e-4a92-942c-1053ac8dacea.png)

---

![image](https://user-images.githubusercontent.com/84378453/214183503-51e06ca1-d253-49fc-8ac4-77c7a6120af5.png)


# Overview

- 一日に与える食事量をご飯のカロリー量から計算する適正食事量計算機能。
- 外観と触感で大まかな太り具合を5段階で判断するBCS計算機能。
- ペットの毎日の様子を写真付きで記録することのできるCRUD機能。
- 犬と柴犬の写真をランダムで表示させる機能。

以上等をまとめdjangoでwebアプリの形にしました。



# サイトURL

https://inunekohealth.up.railway.app/



# Author

- <a href="https://github.com/aohana-AO">https://github.com/aohana-AO</a>
  - CRUD機能
  - バックエンド
  - フロント
  - デプロイ
  - 進捗・タスク管理
  - フロント・バックのエラー修正
  - ロゴ作成
- <a href="https://github.com/hiraku0203">https://github.com/hiraku0203</a>
  - BCS計算
  - 適性食事量計算
  - API処理
  - フロント
  - フロント・バックのエラーチェック
  - README書き



# Requirement

## base
- Python==3.9
- Django==4.1.4
- PyCharm
- visual studio code
- Windows10,11

## CRUD周り
- django-allauth==0.51.0
- django-widget-tweaks==1.4.12

## デプロイ
- gunicorn==20.1.0
- whitenoise==6.2.0
- Railway

## API処理
- requests==2.28.1

## フロント
- js
- jQuery
- BootStorap5.0
- FontAwesome

    
## data

- カロリー計算ロジック[http://www.hidamari-hosp.com/2019/08/24/1411/](http://www.hidamari-hosp.com/2019/08/24/1411/)
- BCS計算ロジック[https://www.env.go.jp/nature/dobutsu/aigo/2_data/pamph/petfood_guide_1808/pdf/6.pdf](https://www.env.go.jp/nature/dobutsu/aigo/2_data/pamph/petfood_guide_1808/pdf/6.pdf)
- サイト[http://gettemplate.com/](http://gettemplate.com/)
- 犬表示API[https://dog.ceo/](https://dog.ceo/)
- 柴犬表示API[https://shibe.online/](https://shibe.online/)


# Description


## 適性食事量計算、BCS計算

### ・外観と触感で大まかな太り具合を5段階で判断するBCSを計算できる
### ・一日に与える食事量をご飯のカロリー量から計算する

![image](https://user-images.githubusercontent.com/84378453/214193415-59ec27fa-42e9-4cbb-b6b2-ace44fc93328.png)


![image](https://user-images.githubusercontent.com/84378453/214193478-995dcead-35f7-409e-9092-49c65866ac06.png)


![image](https://user-images.githubusercontent.com/84378453/214193489-ab1041ef-66c1-4fb8-9abf-52518bc4c294.png)









## CRUD機能
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


# 尽力した点
## 動物病院の情報など参考にBCS計算・適性食事量計算のロジックをプログラムに落とし込んだ。

[https://github.com/hiraku0203/dog-cat_kcal/blob/main/BCS.py](https://github.com/hiraku0203/dog-cat_kcal/blob/main/BCS.py)
    
```Python
 BCS = str()
    
 def animal_bcs(BCS) :

    # 犬か猫か判定
    q1 = int(input("犬なら1、猫なら2を入力: "))

    # 犬🐶
    if q1 == 1 :
        # 肋骨が触れるかどうかで第一段階判断
        rib = int(input("肋骨は触れるか。触れる場合は1を、触れないのなら2を入力: "))

        if rib == 1 :
            # 犬の外観から判断
            look = int(input("肋骨は外観からわかるほどに浮き出ているか。浮き出ているなら1、見えないようなら2を入力: "))

            # 肋骨浮き出るくらい痩せてる
            if look == 1 :
                spine = int(input("脊椎と骨盤も外観からわかり､触っても脂肪がわからないほどに痩せているかどうか。Yesなら1を、Noなら2を入力: "))
                
                if spine == 1 :
                    BCS = "非常にやせ細っています。健康状態や理想体重などの詳しい状態は獣医師に相談して下さい"
                    return BCS
                    
                elif spine == 2 :
                    BCS = "痩せています。理想体重などを獣医師と相談"
                    return BCS

            # そうでもないとき
            elif look == 2 :
                const = int(input("犬を上から見てくびれに注目してください。くびれがはっきりと確認できるのなら1を、すこしある又はあまり見えない場合は2を、全く確認できないなら3を入力: "))
                
                # くびれで判断
                if const == 1 :
                    abdomen = int(input("そのくびれはどの程度か。肋骨あたりからくびれができていて痩せていると感じるのなら1を。肋骨の後ろ、腰のあたりがくびれている場合は2を入力: "))
                    
                    if abdomen == 1 :
                        BCS = "やや瘦せています。理想体重などを獣医師と相談。"
                        return BCS
                    
                    elif abdomen == 2 :
                        BCS = "理想的な体重。おやつのあげすぎなどに注意"
                        return BCS
                
                elif const == 2 :
                    abdomen = int(input("犬を横から見る。そのとき胸からおなかのほうにかけて吊り上がっていっているか。吊り上がっているなら1を、吊り上がっておらず平坦なら2を入力: "))
                    
                    if abdomen == 1 :
                        BCS = "やや肥満気味。適切な運動や食事管理を。おやつのあげすぎには注意"
                        return BCS
                    
                    elif abdomen == 2 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

                elif const == 3 :
                    body = int(input("犬を横から見る。そのときむねからおなかのほうにかけて平坦なら1を、脂肪が垂れ下がるくらいなら2を: "))
               
                    if body == 1 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

                    elif body == 2 :
                        BCS = "かなりの肥満。適切な運動と食事管理を。本格的なダイエットが必要な場合は獣医師に相談"
                        return BCS

        elif rib == 2 :
            body = int(input("犬を横から見る。そのときむねからおなかのほうにかけて平坦なら1を、脂肪が垂れ下がるくらいなら2を: "))
           
            if body == 1 :
                        BCS = "肥満気味。適切な運動と食事管理を。おやつはあげたぶんだけ主食をへらす"
                        return BCS

            elif body == 2 :
                        BCS = "かなりの肥満。適切な運動と食事管理を。本格的なダイエットが必要な場合は獣医師に相談"
                        return BCS


    # ねこ(=^・・^=)
    elif q1 == 2 :

        # 肋骨を触って判断
        rib_touch = int(input("肋骨は簡単に触れるか。Yes=1,No=2: "))
        
        if rib_touch == 1 :
            
            # 外観で
            rib_look = int(input("肋骨は外から見てわかるか。Yes=1,No=2: "))
        
            if rib_look == 1 :
        
                # くびれで
                consta = int(input("肋骨の後ろ、腰のあたりのくびれは深いか。Yes=1,No=2: "))
        
                if consta == 1 :
        
                    body = int(input("横から見て腹部はかなり吊り上がっているか。Yes=1,No=2: "))
        
                    # 結果
                    if body == 1 :
                        BCS = "かなり痩せている。必要なら獣医師に相談"
                        return BCS
                   
                    elif body  == 2 :
                        BCS = "痩せている。"
                        return BCS
        
                elif consta == 2 :
                    BCS = "やや瘦せている。"
                    return BCS

            # くびれの深さで
            elif rib_look == 2 :
                consta = int(input("腰はわずかにでもくびれているか。Yes=1,No=2: "))
        
                if consta == 1 :
                    body = int(input("横から見て腹部の吊り上がりはどの程度か。深いなら1、浅いなら2: "))

                    # 結果
                    if body == 1 :
                        BCS = "やや痩せている。"
                        return BCS

                    elif body == 2 :
                        BCS = "理想体重。"
                        return BCS
                    
                # おなかの丸さで
                elif consta == 2 :
                    body = int(input("横から見ておなかの丸みはどの程度か。やや丸いなら1、まん丸なら2: "))

                    # 結果
                    if body == 1 :
                        BCS = "やや太っている。"
                        return BCS

                    elif body == 2 :
                        body2 = int(input("脇腹のひだは歩くとどれくらい揺れるか。揺れている程度なら1、盛んに揺れるなら2: "))
                        if body2 == 1 :
                            BCS = "太っている。"
                            return BCS

                        elif body2 == 2 :
                            BCS = "かなり太っている。"
                            return BCS


        # 肋骨が触れなかった場合
        elif rib_touch == 2:
            body2 = int(input("脇腹のひだは歩くとどれくらい揺れるか。揺れている程度なら1、盛んに揺れるなら2: "))
            
            if body2 == 1 :
                BCS = "太っている。"
                return BCS

            elif body2 == 2 :
                BCS = "かなり太っている。"
                return BCS


        
            
bcs = animal_bcs(BCS)

print(bcs)
```

## Herokuの有料化、GCP・AWSの個人利用の敷居の高さからデプロイが難しくなっていた点を、Railwayの使用で対処した。
※RailwayへのdjangoデプロイはHerokuへのデプロイの設定を少し弄るだけで可能!

![image](https://user-images.githubusercontent.com/84378453/215642279-afe0fdf8-4305-4dae-955d-f6f8f8e6851d.png)



# 今後について
- Railwayの使用は実際運用の面で制限が多いため、今後このプロダクトを長期運用していく場合は有料プランもしくは他サービスに乗り換えることを検討するべき。
- フロントエンドの幅調整の点で変更しきれてない位置のずれがあったため、この点を改善する必要がある。
- BCS、適性食事量計算の計算結果を保存機能はつける



# Reference
- requirements.txtのpip書き出しについて https://note.nkmk.me/python-pip-install-requirements/

- Railwayを用いたHeroku以外でのdjangoデプロイ https://kikuichige.com/15689/#toc2

- django4.x系列デプロイ後のcsrf検証失敗について https://blog.aoirint.com/entry/2022/django_3_x_to_4_x_csrf_verification_failed/

- Railwayダッシュボード https://railway.app/dashboard

- リポジトリフォーク　https://docs.github.com/ja/get-started/quickstart/fork-a-repo

