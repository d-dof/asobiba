# EM_Algorithm
## 1次元混合正規分布に対するEMアルゴリズムの素朴な実装
[EM_Algorithm.ipynb](https://github.com/sasakamamori/asobiba/blob/master/EM_Algorithm/EM_Algorithm.ipynb)は
1次元混合正規分布のtoy_problemを発生させ, クラスタ数を変えながら最適な混合正規分布モデルを推定し, グラフを書いてその変化を見ていったもの. AICとBICを
用いてモデル選択をできるようにしてある.

[em.py](https://github.com/sasakamamori/asobiba/blob/master/EM_Algorithm/em.py)はグラフまでの描写を勝手に実行するファイル.
モジュール化を一応目論んでいる.
