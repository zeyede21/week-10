from flask import Flask, jsonify
from data_loader import load_brent_data
from change_point_model import build_change_point_model
from analyze_change_points import plot_with_change_point

app = Flask(__name__)

@app.route("/api/change_point", methods=["GET"])
def get_change_point():
    df = load_brent_data()
    trace = build_change_point_model(df['LogReturn'].values, sample_n=1000)
    change_date = plot_with_change_point(df, trace)
    return jsonify({"change_point": str(change_date)})

if __name__ == "__main__":
    app.run(debug=True)
