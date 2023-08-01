#------------------------------------------------------------------------------Hello Everyone-----------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------SEARCH_NEARBY_SHOP-----------------------------------------------------------------------------------------------------------------------------
# This code is not for production purpose. If you want to go in production purpose than rewrite the code as you need.
#こちらのコードはプロダクションには使用できません、使用するのであれば編集してください。
#リポジトリは、GPSを使用してユーザーの現在の位置情報を取得し、その周辺にあるさまざまなショップを一覧化するというコードソースコードを管理しています。
#--------------------------------------------------------------------------------概要-------------------------------------------------------------------------------------------------------------------------------------
#ユーザーが特定のカテゴリ（例：スーパーマーケット、レストラン、薬局など）を選択すると、ユーザーの現在の位置を中心に周辺のショップを検索し、結果を一覧表示します。また、各ショップの住所を提供し、Googleマップへのリンクを提供することで、ユーザーが簡単にショップにアクセスできるようにします。

#------------------------------------------------------------------------------主な機能------------------------------------------------------------------------------------------------------------------------------------
#ユーザーの現在の位置情報を取得
#ユーザーが選択したカテゴリに基づいて周辺のショップを検索
#ショップの名前と住所を一覧表示
#ショップの住所をクリックしてGoogleマップで表示

#------------------------------------------------------------------------------使用技術------------------------------------------------------------------------------------------------------------------------------------
#Python: Webアプリケーションのバックエンド開発に使用
#Flask: Webフレームワークとして使用
#HTML/CSS: フロントエンドのデザインとレイアウトに使用
#JavaScript: ユーザーの位置情報の取得と動的なページ更新に使用
#Google Places API: ショップ情報の検索に使用

#---------------------------------------------------------------------------インストールと実行方法--------------------------------------------------------------------------------------------------------------------------
#Pythonをインストールします（バージョン3以上を推奨）。
#このリポジトリをクローンするか、ZIPファイルとしてダウンロードします。
#リポジトリのディレクトリに移動し、必要なPythonライブラリをインストールします。
#pip install flask requests
#Google Places APIキーを取得し、app.pyファイルのapi_key変数に追加します。
#アプリケーションを起動します。
#Webブラウザでhttp://localhost:5000にアクセスし、アプリケーションを使用します。  

#-----------------------------------------------------------------------その他の注意事項------------------------------------------------------------------------------------------------------------------------------------
カテゴリ（shoptype）の追加や変更は、app.pyファイルの関数get_nearby_places内で行います。
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
