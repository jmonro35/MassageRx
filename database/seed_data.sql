-- data for mySQL tables to pull from when connected to python code

INSERT INTO massage_type(massage_name, massage_description, massage_intensity_level, massage_base_price)
VALUES
('Swedish', 'Spa-style gentle full body massage meant for circulation and relaxation', 'light', 75.00),
('Deep Tissue', 'Targets muscle tension and treatment of deeper muscle tissue', 'firm', 90.00),
('Sports Massage', 'Massage meant for pre-event or post-event muscle recovery to increase circulation', 'medium', 80.00),
('Trigger Point', 'Massage that targets specific localized points of pain as a result of injury or overuse', 'firm', 95.00);

insert into body_area (area_name, region)
values
('Neck', 'upper'),
('Shoulder', 'upper'),
('Elbow', 'upper'),
('Wrist', 'upper'),
('Hand', 'upper'),
('Upper back','upper'),
('Torso', 'full'),
('Back', 'full'),
('Low back', 'lower'),
('Hip', 'lower'),
('Thigh', 'lower'),
('Knee','lower'),
('Calf', 'lower'),
('Foot', 'lower');

-- initial data for keyword table just to make sure python code recognized the words correctly 
insert into symptom_keyword (keyword, weight, rationale, massage_id, area_id)
values
('tight', 10, 'tightness responds well to deep tissue massage', 2, 1); --need to add more data

-- standard safety screening questions for massage therapy
insert into safety_question (question_text, topic, block_message)
values
('Are you currently pregnant?', 'pregnancy', 'Thank you for your response. This facility does not offer prenatal massage. Please contact the facility directly for other recommendations.'),
('Do you have a history of blood clots? i.e deep vein thrombosis', 'blood clots', 'Thank you for your response. Massage therapy may not be recommended at this time. Please contact the facility directly'),
('Have you sustained an injury in the last 48 hours?', 'recent injury', 'Thank you for your response. Massage therapy may not be recommended at this time. Please contact the facility directly'),
('Have you been diagnosed with hypertension?', 'hypertension', 'Thank you for your response. Massage therapy may not be recommended at this time. Please contact the facility directly');

-- reset name for recent injury column after writing recent_injury in python logic
update safety_question
set topic = 'recent_injury'
where topic = 'recent injury';

-- added more key words to table to allow for wider vocabulary 
INSERT INTO symptom_keyword (keyword, weight, rationale, massage_id, area_id)
VALUES
('sore', 8, 'soreness responds well to deep tissue work', 2, 6),
('pain', 7, 'pain relief is a primary benefit of deep tissue massage', 2, 6),
('knot', 9, 'muscle knots are effectively treated with deep tissue pressure', 2, 2),
('tension', 7, 'muscle tension responds well to trigger point therapy', 4, 1),
('stress', 8, 'stress relief is the primary goal of swedish massage', 1, 11),
('relax', 9, 'relaxation is best achieved through swedish massage', 1, 11),
('stiff', 7, 'stiffness responds well to deep tissue work', 2, 1),
('ache', 6, 'general aching benefits from deep tissue massage', 2, 6),
('strain', 8, 'muscle strain responds well to sports massage', 3, 9),
('tired', 6, 'muscle fatigue benefits from swedish massage', 1, 11),
('sport', 9, 'athletic recovery is best supported by sports massage', 3, 11),
('injury', 8, 'injury recovery benefits from sports massage therapy', 3, 9),
('pressure', 7, 'pressure points respond well to trigger point therapy', 4, 2),
('spasm', 9, 'muscle spasms respond well to trigger point therapy', 4, 6),
('burning', 7, 'burning sensation benefits from trigger point release', 4, 2);