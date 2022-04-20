#!/usr/bin/python

from gimpfu import *

def plugin_main(timg, tdrawable, margin=50, gutter=50, panelCount=3, erase=False):
	currentHeight = tdrawable.height
	timg.add_hguide(currentHeight - margin)
	timg.add_hguide(margin)
	timg.add_vguide(margin)
	timg.add_vguide(tdrawable.width-margin)

	currentWidth = tdrawable.width-(margin*2)-(gutter*(panelCount-1))
	panelWidth=(currentWidth/panelCount)
	startPos=margin+panelWidth
	for p in range(panelCount-1):
		timg.add_vguide(startPos)
		timg.add_vguide(startPos+gutter)
		startPos+=panelWidth+gutter



register(
	"photo-panel-guides",
	"Photo panel guides",
	"Photo panel guides",
	"Stovesy",
	"Stovesy",
	"2022",
	"<Image>/Image/Guides/Panel",
	"RGB*, GRAY*",
	[
		(PF_INT, "margin", "Margin", 50),
		(PF_INT, "gutter", "Gutter", 50),
		(PF_INT, "panels", "Panel count", 3),
		(PF_BOOL, "erase", "Erase existing guides", FALSE),
	],
	[],
	plugin_main)

main()