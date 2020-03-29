# 顔写真から猿人類との類似度を判定するアプリケーション

## 目的
・アジア人の顔写真と、日本猿,ゴリラ,チンパンジーの顔写真との類似度を調べる。

## 機能
画像入力フォームで選択した顔写真から、猿人類との類似度をパーセント表示する。

## 入力データ

・学習データ
	Flickr API からスクレイピングした、日本猿,ゴリラ,チンパンジーの画像を、ペイントで顔のみ切り取った画像データ計360枚
	https://www.flickr.com/
・テストデータ
	Flaskで画像入力フォームを作り、そこで選択したアジア人の写真を、OpenCVで顔のみ切り取った画像データ

## 出力データ
「日本猿〇〇％　ゴリラ〇〇％　チンパンジー〇〇％」というように猿人類との類似度をパーセント表示する。

## データフロー
　
・学習データ（Flickr APIで取得） → ペイントで顔を切り取り → Pythonで8:2（訓練データ:検証データ）に分割 → 学習 → Kerasでモデル作成・保存（VGG16の重みを利用）

・画像入力フォームからテストデータ（画像）を選択 → モデルを読み込み → テスト結果を出力

## 使用したモデル、アルゴリズム
　VGG16、CNN

## 環境・言語
例) Windows10, Google Colaboratory, Python3.7(Flask), Atom, GitHub

## ディレクトリの説明  
・doc/ ドキュメント  
・src/ 主なプログラムのソース  
・data/ 画像  
・testdata/ テストデータ  
・tools/ いろいろなツール類
