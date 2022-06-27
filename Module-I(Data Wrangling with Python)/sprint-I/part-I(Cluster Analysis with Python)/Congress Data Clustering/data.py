from collections import defaultdict, Counter
import csv
import glob
from kmeans import k_means, assign_labels
from typing import Dict, List, NamedTuple, DefaultDict, Tuple
from pprint import pprint

NUM_SENATORS = 100

#type annotation
voteValue = int
voteList = List[voteValue]
voteHistory = Tuple[voteValue,...]

vote_value: Dict[str, voteValue]  = {'Yea':1, 'Nay':-1, 'Not Voting':0}
Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
accumulated_record: DefaultDict[Senator, voteList] = DefaultDict(list)                           

for filename in glob.glob('congress_data/*.csv'):
    with open(filename, encoding = "UTF-8") as file:
        reader = csv.reader(file)
        vote_topic = next(reader)
        headers = next(reader)

        #['person', 'state', 'district', 'vote', 'name', 'party']
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote])

#Transform the record into plain dict that maps into tuples
record: Dict[Senator, voteHistory] = {senator: tuple(votes) for senator, votes in accumulated_record.items()}

#use k-means to locate cluster centroids from pattern of votes, assign each senator to the nearest cluster
centroids = k_means(record.values(), k=3)
clustered_votes = assign_labels(centroids, record.values())

# build a reverse mapping from a vote history to a list of senators who voted that way
votes_to_senators = defaultdict(list)

for senator, vote_history in record.items():
    votes_to_senators[vote_history].append(senator)

# run test
assert sum(len(cluster) for cluster in votes_to_senators.values()) == NUM_SENATORS

#display the cluster and members(senators) of each cluster
for i, votes_in_cluster in enumerate(clustered_votes, start=1):
    print(f'====================>cluster num #{i}<====================')
    party_total = Counter()
    for votes in set(votes_in_cluster):
        for senator in votes_to_senators[votes]:
            party_total[senator.party] += 1
            print(senator)
    print(party_total)












