import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Col(
            html.H1("Hypothesis Testing",
            className="text-left"),
            className="mb-5 mt-5"),


        dbc.Col(
                html.H3(children='Dataset',
                className="text-left"),
                className="mb-4 mt-5"),

        dbc.Col(
                html.A(children='Dataset merupakan data history penjualan salah satu perusahaan supermarket yang tercatat di 3 cabang berbeda selama 3 bulan pada tahun 2019. dimana tingkat pertumbuhan supermarket di kota tersebut padat dan semakin meningkat sehingga mengakibatkan persaingan pasar tinggi menjadi tinggi'),
                className="mb-1"),
                html.A(children=[
                      dbc.NavLink("Dataset asli berasal dari kaggle dengan link (Click)", href="https://www.kaggle.com/aungpyaeap/supermarket-sales"),
                ],
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Objective Hypothesis Testing',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Objective Hypothesis Testing adalah dengan melakukan uji statistic terhadap dataset untuk melihat apakah ada kemungkinan hubungan antara pelanggan dengan kategori Member dan Normal (variabel Customer type) dengan gross income yang diterima oleh perusahaan (variabel gross income)'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Metode Hypothesis Testing',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Dalam melakukan Hypothesis Testing, menggunakan metode Chi-Square Test karena variabel yang akan dilakukan pengujian adalah variabel categorikal yaitu variabel Customer type'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Hypothesis',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Dalam analisa hypothesis testing kita ingin menguji apakah ada atau tidaknya kemungkinan hubungan antara pelanggan dengan kategori Member dan Normal (variabel Customer type) dengan gross income yang diterima oleh perusahaan (variabel gross income), sehingga kita dapat menyatakan Hypothesis sebagai berikut:'),
                className="mb-3"
                ),

        dbc.Col(
                html.A(children='- Hypothesis Null (H0) adalah adanya kemungkinan hubungan antara pelanggan dengan kategori Member dan Normal (variabel Customer type) dengan gross income yang diterima oleh perusahaan (variabel gross income),'),
                className="mb-3"
                ),
        dbc.Col(
                html.A(children='- Hypothesis alternatif (H1) adalah tidak ada kemungkinan hubungan antara pelanggan dengan kategori Member dan Normal (variabel Customer type) dengan gross income yang diterima oleh perusahaan (variabel gross income),'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Confidence Interval dan Critical Value',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Dalam analisa ini kita juga menetapkan Confidence Interval sebesar 95% dengan Critical Value sebesar 5%'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Kriteria Hypothesis Testing',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Berikut ini merupakan kriteria suatu Hypothesis diterima atau tidak:'),
                className="mb-3"
                ),

        dbc.Col(
                html.A(children='- Hypothesis Null (H0) diterima, apabila uji statistik berada diluar Critical Value,'),
                className="mb-3"
                ),
        dbc.Col(
                html.A(children='- Hypothesis alternatif (H1) diterima, apabila uji statistik berada di dalam Critical Value,'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Hypothesis Testing',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='dari hasil Hypothesis Testing didapatkan hasil p-value sebesar 1.0'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='Kesimpulan Hypothesis Testing',
            className="text-left"),
            className="mb-4 mt-5"),
        dbc.Col(
                html.A(children='Dari Hasil Hypotesis Testing di peroleh hasil dan kesimpulan sebagai berikut:'),
                className="mb-3"
                ),

        dbc.Col(
                html.A(children='- Hypothesis (H0) diterima, sehingga dapat disimpulkan adanya kemungkinan hubungan antara pelanggan dengan kategori Member dan Normal (variabel Customer type) dengan gross income yang diterima oleh perusahaan (variabel gross income)'),
                className="mb-3"
                ),
        dbc.Col(
                html.A(children='- Hypothesis (H0) diterima karena nilai uji statistik (p_value) sebesar 1 lebih besar dari nilai Critical Value sebesar 5%'),
                className="mb-7"
                ),

        dbc.Col(
            html.H3(children='',
            className="text-left"),
            className="mb-4 mt-5"),


    ])

])
