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

insert into symptom_keyword (keyword, weight, rationale, massage_id, area_id)
values
('tight', 10, 'tightness responds well to deep tissue massage', 2, 1); --need to add more data