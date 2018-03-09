from django import forms

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

REMEMBER TO INCREMENT `mow_direction` OF TurfFeature INSTANCE WHEN APPLYING A
MOWING INSTANCE TO IT!!!!!!!!!


For greens

	mow_direction += pi / 4
	if mow_direction >= pi:
		mow_direction -= pi

For tees

	mow_direction += pi / 4
	if mow_direction == pi / 2:
		mow_direction += pi / 4
	if mow_direction >= pi:
		mow_direction -= pi

For fairways

	mow_direction += pi / 2
	if mow_direction >= pi:
		mow_direction -= pi

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""