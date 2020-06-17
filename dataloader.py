import codecs
import os
import tqdm

def loader(config_path):
    ds = []
    with open(os.path.join(config_path, "data/train.to")) as t, open(os.path.join(config_path, "data/train.from")) as f:
        fr = f.readlines()
        to = t.readlines()
        for i in tqdm.tqdm(range(len(fr))):
            if "removed" in fr[i] or "deleted" in fr[i] or "removed" in to[i] or "deleted" in to[i] or not fr[i] or not to[i] :
                continue
            ds.append(fr[i])
            ds.append(to[i])
    
    f = codecs.open(os.path.join(config_path, "data/training_data.txt"), "w", "utf-8")
    for ele in ds:
        f.write(ele)
    f.close()

if __name__ == '__main__':
    loader(".")
