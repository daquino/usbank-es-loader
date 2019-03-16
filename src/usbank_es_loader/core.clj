(ns usbank-es-loader.core)
(require '[clojure-csv.core :as csv]
         '[clojure.java.io :as io])

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))

(defn -main [& args]
  "Loads US Bank transactions into an Elasticsearch index.  The data source comes from a .csv
  file downloaded from the US Bank website.

  The format of the file is:

  Date,Transaction Type(DEBIT/CREDIT),Description,Memo,Amount
  "
  (let [filename (first args)]
    (with-open [reader (io/reader filename)]
      (doseq [item (next (csv/parse-csv reader))]
        (let [[timestamp transaction-type description memo amount] item
              a (bigdec amount)]
          (println "Timestamp: " timestamp " Amount: " a))))))
