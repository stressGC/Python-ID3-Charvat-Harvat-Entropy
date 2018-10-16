from id3 import Id3Estimator
from sklearn.datasets import fetch_kddcup99
from sklearn.model_selection import train_test_split
from id3 import export_graphviz
import numpy as np

bunch = fetch_kddcup99(subset="SA")

data = bunch.data
data = np.delete(data, np.s_[1:4], axis=1)
target = bunch.target
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=.2, random_state=17)

estimator = Id3Estimator()
print("->Fitting ID3 classifier")
estimator.fit(X_train, y_train)

print("->reating dot file")
export_graphviz(estimator.tree_, 'tree.dot')

print("->Calculating predictions")
pred = estimator.predict(X_test)

well_detected = 0
for index, val in enumerate(pred):
	if val == y_test[index]:
		well_detected += 1

percentage = well_detected / len(pred) * 100
print("predictions: ", well_detected, "/", len(pred), " = ", percentage, "%")









"""
col_names = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label']

print("loading dataset")
df = pd.read_csv("id3/data/t.csv", header=None, names=col_names)
target = df["label"]
data = df.drop(columns=["label"])
bunch = load_breast_cancer()
print("df", df.head())
print("data", bunch.data)
print("ourdata", data)
print("target", bunch.target)
print("ourtarget", target)
estimator = Id3Estimator()
estimator.fit(data, target)
print(estimator)
"""