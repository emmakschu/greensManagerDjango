from collections import Counter
from courses import models as Courses 

def mode(some_list):
	c = Counter(some_list)
	return c.most_common(1)[0][0]

def build_dir_list(model_objects):
	directions = []

	for instance in model_objects:
		directions.append(instance.mow_direction)

	return directions

def greens_mow_direction():
	greens = Courses.Green.objects.all()
	greens_dirs = build_dir_list(greens)
	return mode(greens_dirs)

def tee_mow_direction():
	tees = Courses.Tee.objects.all()
	tee_dirs = build_dir_list(tees)
	return mode(tee_dirs)

def fairway_mow_direction():
	fairways = Courses.Fairway.objects.all()
	fairway_dirs = build_dir_list(fairways)
	return mode(fairway_dirs)