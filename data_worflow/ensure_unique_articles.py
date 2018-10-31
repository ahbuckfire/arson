from sklearn.feature_extraction.text import TfidfVectorizer

import elastic

def search_index(es, index="bing", doc="bing"):
    res = es.search(index=index, doc_type=doc, q="*", size=100)
    return res["hits"]["hits"]


def get_text_bodies(query_results):
    return [r["_source"]["all_text"] for r in query_results]


def calculate_cosine_similarity(texts):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(texts)
    return (tfidf * tfidf.T).A


def get_top_cases(cos_sim, query_results, num_cases=5, threshold=0.1):
    indices = []
    curr_article = 0
    for idx, case in enumerate(cos_sim):
        if len(indices) < num_cases:
            for j in range(1, len(cos_sim) - idx):
                if abs(case[idx] - case[idx + j]) > threshold:
                    indices.append(idx)
                    break
        else:
            break

    return [query_results[index]["_source"] for index in indices]


def get_non_duplicate_articles():
    es = elastic.connect_elasticsearch()
    query_results = search_index(es)
    cos_sim = calculate_cosine_similarity(get_text_bodies(query_results))
    return get_top_cases(cos_sim, query_results)
