from unittest.mock import Mock
import statistics

# Mocking structure_manager and its methods
structure_manager_mock = Mock()

# Create mock class items
house_mock = Mock()
house_mock.unique_id = "House"
house_mock.full_name = "House"
house_mock.get_all_occurrence_values.return_value = [2, 1]  # House has links with OrangeCat and CatBehavior
house_mock.get_filtered_git_links.return_value = ["OrangeCat", "CatBehavior"]
house_mock.get_nr_of_occ_with.side_effect = lambda x: 2 if x == "OrangeCat" else 1  # House-OrangeCat: 2, House-CatBehavior: 1
house_mock.commits_count = 2  # Total number of commits involving House

orange_cat_mock = Mock()
orange_cat_mock.unique_id = "OrangeCat"
orange_cat_mock.full_name = "OrangeCat"
orange_cat_mock.get_all_occurrence_values.return_value = [2, 3]  # OrangeCat has links with House and CatBehavior
orange_cat_mock.get_filtered_git_links.return_value = ["House", "CatBehavior"]
orange_cat_mock.get_nr_of_occ_with.side_effect = lambda x: 2 if x == "House" else 3  # OrangeCat-House: 2, OrangeCat-CatBehavior: 3
orange_cat_mock.commits_count = 4  # Total number of commits involving OrangeCat

cat_behavior_mock = Mock()
cat_behavior_mock.unique_id = "CatBehavior"
cat_behavior_mock.full_name = "CatBehavior"
cat_behavior_mock.get_all_occurrence_values.return_value = [1, 3]  # CatBehavior has links with House and OrangeCat
cat_behavior_mock.get_filtered_git_links.return_value = ["House", "OrangeCat"]
cat_behavior_mock.get_nr_of_occ_with.side_effect = lambda x: 1 if x == "House" else 3  # CatBehavior-House: 1, CatBehavior-OrangeCat: 3
cat_behavior_mock.commits_count = 3  # Total number of commits involving CatBehavior

# Setup entity_class_id_dict to return these mock items when their IDs are used
entity_class_id_dict = {
    "House": house_mock,
    "OrangeCat": orange_cat_mock,
    "CatBehavior": cat_behavior_mock
}

# Mock get_class_list to return a list of mock class items
structure_manager_mock.get_class_list.return_value = [house_mock, orange_cat_mock, cat_behavior_mock]

# Define the mocked version of count_strength function with threshold set to 60
def count_strength(structure_manager, pos, threshold=60):
    entity_class_id_dict = {}
    max_occ_list = []

    for classItem in structure_manager.get_class_list():
        entity_class_id_dict[classItem.unique_id] = classItem
        values = classItem.get_all_occurrence_values()
        max_occ = 0
        if values:
            max_occ = max(values)
        max_occ_list.append(max_occ)

    mean = statistics.mean(max_occ_list)
    print(max_occ_list)
    print(mean)

    if mean:
        entities_count = 0
        try:
            for classItem in structure_manager.get_class_list():
                entity1 = classItem

                related_list = classItem.get_filtered_git_links(1)
                for entity2_id in related_list:
                    entity2 = entity_class_id_dict[entity2_id]

                    freqAUB = entity1.get_nr_of_occ_with(entity2_id)  # commits involving A and B
                    freqA = entity1.commits_count  # total nr of commits involving A

                    strength = freqAUB / mean

                    confidence_percent = ((100 * freqAUB) / freqA) * strength
                    print(f"{entity1.full_name},{entity2.full_name},{confidence_percent}, LD")
                    if confidence_percent >= threshold:
                        entities_count += 1

        except BaseException as e:
            print("Exception: " + str(e))

    # Print the results count
    results_count = {}
    results_count[pos] = entities_count
    print("Count git links with strength " + str(threshold) + "% ...")
    print("Entities Count:", results_count[pos])

# Run the mocked function
count_strength(structure_manager_mock, pos=0)