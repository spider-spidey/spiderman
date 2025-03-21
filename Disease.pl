disease(diabetes, low_carb).
disease(hypertension, low_sodium).
disease(obesity, low_calorie).
disease(anemia, iron_rich).
disease(osteoporosis, calcium_rich).
disease(celiac, gluten_free).
disease(heart_disease, low_fat).
disease(kidney_disease, low_protein).

diet(low_carb, ['Green Vegetables', 'Eggs', 'Fish', 'Nuts']).
diet(low_sodium, ['Fresh Fruits', 'Leafy Greens', 'Oats', 'Brown Rice']).
diet(low_calorie, ['Vegetables', 'Fruits', 'Lean Meat', 'Whole Grains']).
diet(iron_rich, ['Spinach', 'Liver', 'Legumes', 'Red Meat']).
diet(calcium_rich, ['Milk', 'Yogurt', 'Cheese', 'Leafy Greens']).
diet(gluten_free, ['Rice', 'Corn', 'Quinoa', 'Vegetables']).
diet(low_fat, ['Fish', 'Chicken', 'Vegetables', 'Oats']).
diet(low_protein, ['Rice', 'Pasta', 'Vegetables', 'Apples']).

suggest_diet(Disease) :-
    disease(Disease, DietType),
    diet(DietType, Foods),
    write('Recommended diet for '), write(Disease), write(' is: '), nl,
    write('Diet Type: '), write(DietType), nl,
    write('Foods: '), write(Foods), nl.
