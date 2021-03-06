# Data mining
### ID3 with Harvat - Charvat entropy

The work of this repo is based on the python module [decision-tree-id3](http://https://svaante.github.io/decision-tree-id3 "decision-tree-id3") by **svaante**. It is a module created to derive decision trees using the
ID3 algorithm. It is written to be compatible with Scikit-learn's API
using the guidelines for Scikit-learn-contrib. It is licensed under the
3-clause BSD license.

## Installation

#### Dependencies

- [Python](https://www.python.org/downloads/ "download Python") (>= 2.7 or >= 3.3) 
- NumPy (>= 1.6.1)
- Scikit-learn (>= 0.17)

```bash
pip install numpy
pip install scipy
pip install scikit-learn
```

#### Local installation
Clone the project using:
```bash
git clone https://github.com/stressGC/data-mining-id3-custom.git
cd data-mining-id3-custom/decision-tree-id3
python setup.py install
```

## Usage

If the installation is successful, you should be able to execute the
following Python script:

```bash
python script.py
```

This script uses our custom ID3 implementation based on Harvat & Charvat's entropy. We used the KDDCup99 dataset included in SKLean. We firstly split the data into train and test sets (80 and 20%). Once the model is computed, the tree is exported as a .dot file (tree.dot), this file can be transformed into an image online. The result is in the repo as tree.pdf.

We wrote the [script](https://github.com/stressGC/data-mining-id3-custom/blob/master/decision-tree-id3/script.py "script.py") to merge all the logic and dependencies. The changes made on the entropy's calculations have been made in the file [splitter.py](https://github.com/stressGC/data-mining-id3-custom/blob/master/decision-tree-id3/id3/splitter.py "splitter.py") under the function named *\_entropy*. We left the basic ID3's entropy calculation commented.

We achieved having 96.56% of well-detected attacks.

## LAB 01 - Georges Cosson & Antoine Demon

#### Question 1 :  Faire la synthèse de l’[article](https://github.com/stressGC/data-mining-id3-custom/blob/master/article.pdf "article") ?

L’article traite de la détection de tentatives d’intrusion dans un système informatique en nous présentant un classeur issu de l’algorithme ID3. Selon l’article, ce classeur est bien plus puissant que les classeurs existants jusqu’alors. L’utilisation de l’algorithme ID3 permet aux classeurs d’apprendre à différencier les requêtes issues d’une utilisation normale de celles issues d’une attaque.

Dans cet article, on introduit la notion d’une constante ‘alpha’ dont la valeur est comprise entre 0 et 1. Cette constante influe sur une partie de l’algorithme. Le jeu de données utilisé est issu de la DARPA, Defense Advanced Research Projects Agency, agence de recherche et développement dans le domaine militaire. Ce jeu de données contient plus de cinq millions d’instances.

Pour définir les règles d’intrusion, on utilise l’entropie d’Harvat et Charvat à la place de l’entropie de Shannon comme c’est le cas avec ID3. Le résultat expérimental nous montre qu’un un algorithme de détection d’intrusion basé sur l’algorithme ID3 est réalisable, efficace, et il est surtout très précis. La prochaine étape pour les chercheurs sera de pouvoir détecter une intrusion le plus précisément possible afin qu’aucune ne passe à travers les mailles du filet.


#### Question 2 : Modifier l’algorithme ID3 en utilisant l’entropie d’Harvat et Charvat décrite dans l’article « Intrusion detection and classification using improved ID3 algorithm of data mining »

Voir ci-dessus.

#### Question 3 : Expérimenter cette nouvelle implantation en utilisant la même base de données « KDD99 » sur la détection d’intrusion et le protocole de validation décrit dans l’article. Expliquez comment vous avez procédé pour l’échantillonnage et la manière dont vous avez mené les tests.

Pour l'échantillonage nous avons utilisé un **train/test split** de ratio 80/20% disponible via la librairie SKLearn. Nous avons fait varier ce ratio de 50/50% à 90/10%, en gardant les meilleurs résultats: 80/20%. Nous avons calculé le taux de détection avec la formule suivante :

```detection_rate = number_of_correctly_predicted * 100 / total_number_of_instances```

Le taux d'error peut se calculer d'après ```1 - detection_rate```.

L'arbre obtenu est le suivant : 

![Arbre obtenu](https://github.com/stressGC/data-mining-id3-custom/blob/master/tree.png "obtained tree")

Il est disponible en format [PDF](https://github.com/stressGC/data-mining-id3-custom/blob/master/tree.pdf "Tree as PDF"). Il est obtenu en convertissant le fichier **.dot** généré en pdf.

#### Question 4 : Est-ce-que vous avez obtenu les mêmes résultats que l’article ? Si ce n’est pas le cas, justifiez votre réponse ? Expliquez pourquoi cette nouvelle entropie d’Harvat et Charvat donne une meilleure solution ?

Nous avons obtenu un taux de détection quasiment similaire à celui de l'article de 96.55%. La légère différence peu s'expliquer par les choix que nous avons fait pour séparer le dataset en train & test. De plus, nous avons utilisé le dataset de SKLearn qui n'a pas forcément exactement les mêmes entrées que celui de l'article. Finalement, nous ne groupons pas la classification par type d'attaque ou par attaque ou non, ce qui expliqué des résultats un peu inférieurs.

![Résultats](https://github.com/stressGC/data-mining-id3-custom/blob/master/results.PNG "script results")

L’entropie de Shannon, utilisée pour l’algorithme ID3, donne des résultats complexes, ainsi qu'un nombre très important de nœuds, de feuilles et de règles de décision. Cela implique une perte de temps dans la classification de l'algorithme.

En utilisant l’entropie de Harvat et Charvat à la place de l’entropie de Shanon, les résultats sont plus simples, le nombre de nœuds et de règles de décision est réduit, impliquant une classification plus rapide.

#### Question 5 : Quelle est la valeur optimale du paramètre « alpha ». Expliquez, comment vous avez procédé pour obtenir cette valeur ?

Nous avons lancé le script de classification à l'intérieur d'une boucle, modifiant la valeur d'*alpha* à chaque itération. Nous avons fait varier *alpha* avec un pas de 0.05 allant de 0.05 à 0.95. Nous avons gardé le taux de performance le plus élevé. La valeur optimale que nous avons trouvé est de **0.5** pour *alpha*.


