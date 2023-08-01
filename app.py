from flask import Flask, render_template, request
import requests

app = Flask(__name__) #Flaskアプリケーションのインスタンスを生成

api_key = 'AIzaSyDnayTrEZND71qisosLhuquBPHUMAvE2Hw' #Google Maps Places APIのAPIキーを設定(入力してください)

def get_nearby_places(latitude, longitude, radius):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json' ##Google Maps Places APIのエンドポイントを指定
    params = {
        'location': f'{latitude},{longitude}', #Google Maps Places APIのエンドポイントを指定
        'radius': radius, #検索半径をパラメータに追加
        'key': api_key, #APIキーをパラメータに追加
        'language': 'ja', #言語を日本語に設定
    }

# APIへGETリクエストを送信し、レスポンスをJSON形式で解析
    try:
        response = requests.get(url, params=params)  #リクエストを送信してレスポンスを取得
        data = response.json() #レスポンスをJSON形式に解析してdataに格納

# APIへGETリクエストを送信し、レスポンスをJSON形式で解析
        if response.status_code == 200 and data['status'] == 'OK': #レスポンスのステータスコードが200（成功）で、dataの'status'キーが'OK'（成功）の場合
            return data.get('results', []) #dataの'results'キーに対応する値を取得して返す。なければ空のリストを返す。
        else:
            print(f"Failed to fetch nearby places. Status Code: {response.status_code}, Error Message: {data.get('status')}") #dataの'results'キーに対応する値を取得して返す。なければ空のリストを返す。

    except requests.exceptions.RequestException as e: #requestsのリクエスト例外が発生した場合
        print(f"An error occurred while making the API request: {e}") #APIリクエストの際にエラーが発生した場合、エラーメッセージをコンソールに表示
    
    return [] #外が発生した場合やデータ取得が失敗した場合は、空のリストを返す

# 場所のPlace IDを使用して、店舗のウェブサイトURLを取得する関数
def get_shop_url(place_id): #get_shop_urlという名前の関数を定義し、引数としてplace_idを受け取る
    url = f'https://maps.googleapis.com/maps/api/place/details/json' #Google Maps Places APIの詳細情報エンドポイントのURLを指定
    params = {
        'place_id': place_id, #place_idをパラメータとして追加
        'key': api_key #APIキーをパラメータとして追加
    }

# 場所のPlace IDを使用して、店舗のウェブサイトURLを取得する関数
    try:
        response = requests.get(url, params=params) #APIエンドポイントにGETリクエストを送信し、レスポンスを取得
        data = response.json() #レスポンスをJSON形式に解析してdataに格納


# リクエストが成功したかどうかを確認し、ウェブサイトURLを返す
        if response.status_code == 200 and data['status'] == 'OK': #レスポンスのステータスコードが200（成功）で、dataの'status'キーが'OK'（成功）の場合
            if 'result' in data and 'website' in data['result']: #dataの中に'result'キーがあり、その中に'website'キーがある場合
                return data['result']['website'] #dataの'result'キーの中の'website'キーに対応する値（店舗のウェブサイトURL）を返す
            else:
                print("Shop URL not found in the API response.") #店舗のウェブサイトURLがAPIのレスポンスに見つからない場合、メッセージをコンソールに表示
        else:
            print(f"Failed to fetch shop details. Status Code: {response.status_code}, Error Message: {data['status']}") #店舗の詳細情報を取得できなかった場合、エラーメッセージをコンソールに表示

    except requests.exceptions.RequestException as e: #requestsのリクエスト例外が発生した場合
        print(f"An error occurred while making the API request: {e}") #APIリクエストの際にエラーが発生した場合、エラーメッセージをコンソールに表示
    
    return None #エラーが発生した場合や店舗のウェブサイトURLが見つからなかった場合、None（何も返さない）を返す

# リクエストが成功したかどうかを確認し、ウェブサイトURLを返す
def get_shop_address(place_id): #get_shop_addressという名前の関数を定義し、引数としてplace_idを受け取る
    url = f'https://maps.googleapis.com/maps/api/place/details/json' #get_shop_addressという名前の関数を定義し、引数としてplace_idを受け取る
    params = {
        'place_id': place_id, #place_idをパラメータとして追加
        'fields': 'formatted_address', #フォーマットされた住所のみを取得するように、'fields'パラメータに'formatted_address'を追加
        'key': api_key, #APIキーをパラメータとして追加
        'language': 'ja', #言語を日本語に設定
    }

 # APIへGETリクエストを送信し、レスポンスをJSON形式で解析
    try:
        response = requests.get(url, params=params) #APIエンドポイントにGETリクエストを送信し、レスポンスを取得してresponse変数に格納
        data = response.json() #レスポンスをJSON形式に解析してdata変数に格納

 # リクエストが成功したかどうかを確認し、フォーマットされた住所を返す
        if response.status_code == 200 and data['status'] == 'OK': #レスポンスのステータスコードが200（成功）で、dataの'status'キーが'OK'（成功）の場合
            if 'result' in data and 'formatted_address' in data['result']: #dataの中に'result'キーがあり、その中に'formatted_address'キーがある場合
                return data['result']['formatted_address'] #dataの'result'キーの中の'formatted_address'キーに対応する値（フォーマットされた住所）を返す
            else:
                print("Shop address not found in the API response.") #店舗の住所がAPIのレスポンスに見つからない場合、メッセージをコンソールに表示
        else:
            print(f"Failed to fetch shop address. Status Code: {response.status_code}, Error Message: {data['status']}") #店舗の住所を取得できなかった場合、エラーメッセージをコンソールに表示

    except requests.exceptions.RequestException as e: #requestsのリクエスト例外が発生した場合
        print(f"An error occurred while making the API request: {e}") #APIリクエストの際にエラーが発生した場合、エラーメッセージをコンソールに表示

    return None #エラーが発生した場合や店舗の住所が見つからなかった場合、または例外が発生した場合は、None（何も返さない）を返す

# カテゴリーによって場所（店舗）をフィルタリングする関数
def filter_by_shoptype(places, shoptype): #filter_by_shoptypeという名前の関数を定義し、引数としてplacesとshoptypeを受け取る
    if not shoptype or shoptype == "all": #shoptypeが空文字列または"all"の場合
        return places #全ての店舗情報をそのまま返す（フィルタリングしない）

    # プレイスの'types'属性に指定のshoptypeが含まれている場所のみをフィルタリングして返す
    filtered_places = [place for place in places if shoptype in place.get("types", [])] #placesリスト内の各placeに対して、placeの'types'属性にshoptypeが含まれている場合のみをfiltered_placesに含める
    return filtered_places #フィルタリングされた店舗情報を返す

# インデックスページのルートを定義
@app.route('/', methods=['GET', 'POST'])
def index(): #'/'ルートに対するGETとPOSTメソッドの両方のリクエストに応答するindex関数を定義
    if request.method == 'POST': #リクエストがPOSTメソッドの場合
        # POSTリクエスト（送信されたフォームデータ）からデータを取得
        data = request.get_json() #POSTリクエストのJSONデータを取得してdata変数に格納
        radius = int(data['radius']) #フォームから送信された半径データを整数に変換してradius変数に格納
        latitude = float(data['latitude']) #フォームから送信された緯度データを浮動小数点数に変換してlatitude変数に格納
        longitude = float(data['longitude']) #フォームから送信された経度データを浮動小数点数に変換してlongitude変数に格納
        shoptype = data['shoptype']  # フォームから送信された選択されたカテゴリ（店舗の種類）をshoptype変数に格納

        # 現在の位置と指定された半径に基づいて近隣の場所（店舗）を取得
        nearby_places = get_nearby_places(latitude, longitude, radius)

         # カテゴリーによって場所をフィルタリング
        filtered_places = filter_by_shoptype(nearby_places, shoptype)

        # 場所のPlace IDを使用して近隣の店舗のウェブサイトURLと住所を取得
        shop_details = []
        for place in filtered_places: #フィルタリングされた場所のリストに対してループ
            shop_url = get_shop_url(place['place_id']) #場所のPlace IDを使って店舗のウェブサイトURLを取得
            shop_address = get_shop_address(place['place_id']) #場所のPlace IDを使って店舗のウェブサイトURLを取得
            if shop_url and shop_address: #ウェブサイトURLと住所がともに取得された場合
                shop_details.append({"name": place['name'], "url": shop_url, "address": shop_address})
        
        # フィルタリングされた店舗の詳細情報と選択されたカテゴリーを結果のテンプレートに渡す
        return render_template('result.html', shops=shop_details, shoptype=shoptype)  # Pass the category and address to the template
    else:
        # GETリクエスト（初期ページロード）時にインデックスのテンプレートをレンダリング
        return render_template('index.html') #フォームが未送信の状態でページがロードされた場合に、index.htmlテンプレートをレンダリング
    
# このスクリプトが直接実行された場合、Flaskアプリを実行
if __name__ == "__main__": #このスクリプトが直接実行された場合、Flaskアプリを実行
    app.run(debug=True) #アプリをデバッグモードで実行

#This code is not for production olny use for internal use. If you want to use this code in production level than, you much changes the codes.
#こちらのコードはプロダクションレベルで使用するコードではありません。プロダクションレベルで使用するならば編集行なってください。