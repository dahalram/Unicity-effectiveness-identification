from itertools import chain
from itertools import combinations

#DATA KHAKI;
#INPUT control_number 0 1 2 3;

a = '''0,0,4,1,3,4
1,0,3,2,4,3
2,1,4,1,0,4
3,2,2,3,4,0
4,2,2,1,4,2
5,4,2,3,3,1
6,2,0,3,0,4
7,0,0,2,4,1
8,0,4,1,0,3
9,2,4,1,4,3
10,2,0,1,0,2
11,2,3,1,0,1
12,0,0,4,4,4
13,3,0,0,0,4
14,3,1,4,4,0
15,0,4,2,4,0
16,2,2,0,3,4
17,2,1,0,4,4
18,0,2,1,2,0
19,0,3,1,0,4
20,2,2,1,4,3
21,1,4,1,3,0
22,4,3,1,1,2
23,3,1,1,0,1
24,3,1,4,0,2
25,1,2,0,1,1
26,1,3,4,1,2
27,3,3,1,2,4
28,4,3,4,4,2
29,4,0,0,4,1
30,0,3,3,1,4
31,1,3,0,1,1
32,4,3,1,1,2
33,0,4,3,0,1
34,2,3,0,0,0
35,1,2,3,1,0
36,1,3,2,3,0
37,4,3,0,4,4
38,2,1,1,0,3
39,0,4,1,0,0
40,0,2,1,2,3
41,2,3,3,1,4
42,4,0,4,0,3
43,0,0,4,3,0
44,0,2,0,0,2
45,0,1,2,4,0
46,2,3,1,3,2
47,1,0,3,3,0
48,0,4,0,2,2
49,1,4,2,0,0
50,3,0,0,2,2
51,1,0,3,3,1
52,2,3,0,1,0
53,2,4,2,1,2
54,2,0,1,1,3
55,4,3,1,2,1
56,4,4,2,2,2
57,0,3,2,1,4
58,3,3,0,0,0
59,4,2,3,3,2
60,3,4,4,2,3
61,4,0,3,1,3
62,4,3,0,4,4
63,2,4,2,0,1
64,3,2,1,1,2
65,3,1,0,1,1
66,2,2,3,2,2
67,1,2,4,3,3
68,1,3,0,0,2
69,0,2,2,2,0
70,1,2,3,1,4
71,1,2,0,1,0
72,3,3,2,0,3
73,0,0,2,1,3
74,2,2,0,2,3
75,3,3,2,4,0
76,4,0,2,2,1
77,1,3,3,3,0
78,0,1,3,3,0
79,0,0,3,3,1
80,2,3,3,3,2
81,4,3,4,0,2
82,4,4,1,3,0
83,2,1,2,0,0
84,2,0,3,0,1
85,4,1,1,4,0
86,1,1,2,3,0
87,4,0,0,3,3
88,1,2,2,1,4
89,1,2,1,4,1
90,1,0,0,3,0
91,1,0,3,2,4
92,1,1,3,2,1
93,0,2,2,4,1
94,0,3,0,2,2
95,3,3,4,3,3
96,0,2,0,0,4
97,2,0,3,3,2
98,1,3,3,3,2
99,4,1,2,4,1
100,2,3,3,4,3
101,3,4,4,1,4
102,2,3,1,0,1
103,0,1,0,1,1
104,1,4,2,4,1
105,3,2,3,2,2
106,2,1,1,4,1
107,0,3,3,0,1
108,4,0,3,3,0
109,2,2,4,4,2
110,3,2,0,0,2
111,3,0,2,4,2
112,2,0,1,1,4
113,3,2,0,0,0
114,4,2,4,2,4
115,3,1,3,3,2
116,0,2,4,2,4
117,1,4,0,2,3
118,1,1,0,4,1
119,2,0,1,1,0
120,0,4,1,3,1
121,2,1,3,1,3
122,3,3,1,1,3
123,0,4,4,3,3
124,3,2,0,1,0
125,1,3,1,0,3
126,0,4,2,2,4
127,4,2,2,1,4
128,0,4,0,4,0
129,2,0,0,4,0
130,4,4,2,3,1
131,4,2,1,1,2
132,4,2,0,0,0
133,3,3,1,4,4
134,3,1,2,3,1
135,0,4,1,4,0
136,2,2,1,0,0
137,0,1,2,2,4
138,3,2,0,0,1
139,0,0,3,3,0
140,3,2,3,4,0
141,3,2,3,4,4
142,3,4,2,3,0
143,4,1,4,2,4
144,1,2,2,4,1
145,2,1,2,3,1
146,3,0,2,3,0
147,4,2,2,3,4
148,4,0,4,4,3
149,4,2,0,4,0
150,0,1,3,2,1
151,2,3,0,0,1
152,0,0,2,4,2
153,4,3,1,1,1
154,3,1,0,3,0
155,0,1,1,3,2
156,1,0,1,4,2
157,2,0,1,2,0
158,1,4,1,0,0
159,3,1,3,4,1
160,4,1,3,2,4
161,4,0,4,3,2
162,3,2,1,1,0
163,4,0,2,0,0
164,1,3,2,2,0
165,2,3,0,2,1
166,2,3,3,3,4
167,0,0,0,4,0
168,3,3,0,4,1
169,1,4,1,4,1
170,1,0,3,2,0
171,3,3,4,0,3
172,4,1,2,4,2
173,1,2,3,3,1
174,4,0,4,1,4
175,3,0,2,4,3
176,0,4,1,1,1
177,3,2,0,1,4
178,2,1,1,2,1
179,1,0,2,4,0
180,3,3,0,4,1
181,0,3,4,0,4
182,1,4,2,4,0
183,2,3,3,4,4
184,3,2,2,0,0
185,3,0,1,3,0
186,3,2,0,4,3
187,1,1,1,0,4
188,2,2,4,4,1
189,1,3,0,4,0
190,4,2,4,1,2
191,3,2,4,0,0
192,1,2,1,3,0
193,4,1,0,4,3
194,1,4,1,1,3
195,1,2,4,2,0
196,1,0,0,0,4
197,2,1,0,0,0
198,3,4,0,1,0
199,2,2,1,2,4
200,2,1,0,3,0
201,0,4,0,4,4
202,3,2,2,3,4
203,0,2,0,3,1
204,4,4,3,3,3
205,1,4,3,3,3
206,4,4,1,0,1
207,2,4,2,2,2
208,1,0,4,0,3
209,3,2,3,1,4
210,2,0,4,1,2
211,0,3,4,2,3
212,3,4,1,0,0
213,1,0,1,1,1
214,1,4,2,4,0
215,1,1,1,2,1
216,1,1,3,0,4
217,4,3,2,0,3
218,1,3,3,3,1
219,3,1,2,2,3
220,4,0,3,4,1
221,4,4,1,2,0
222,3,0,0,4,0
223,3,1,2,1,1
224,1,4,0,3,4
225,0,4,2,1,4
226,3,3,1,3,0
227,4,3,4,3,0
228,0,4,0,4,2
229,1,2,0,1,4
230,1,0,2,3,4
231,4,4,1,1,1
232,4,2,4,0,1
233,3,1,0,2,3
234,2,0,2,3,0
235,1,3,3,2,2
236,0,4,1,0,2
237,2,4,4,4,3
238,0,0,3,0,4
239,2,0,2,2,1
240,2,0,0,3,1
241,4,3,2,2,4
242,1,2,4,4,2
243,2,2,3,1,1
244,0,2,0,3,2
245,1,0,4,2,1
246,0,4,2,3,1
247,1,4,0,2,0
248,4,4,1,1,2
249,3,3,3,1,3
250,2,0,0,1,2
251,3,1,4,2,0
252,1,4,2,0,3
253,4,4,4,3,3
254,3,0,2,4,2
255,0,3,3,4,1
256,2,4,3,4,3
257,0,3,1,2,3
258,1,4,1,2,1
259,4,4,4,1,3
260,4,2,3,4,2
261,2,4,3,4,2
262,2,3,1,4,1
263,0,1,0,2,3
264,4,1,4,2,4
265,0,1,1,3,0
266,0,2,3,3,3
267,2,4,3,4,0
268,2,3,2,4,4
269,4,3,0,3,3
270,2,1,2,3,1
271,3,1,4,4,1
272,3,3,3,3,3
273,3,1,1,2,1
274,4,0,0,1,4
275,0,1,1,1,2
276,1,3,0,2,4
277,3,0,2,0,2
278,1,2,0,1,0
279,1,3,0,2,1
280,1,1,1,0,0
281,3,0,2,0,4
282,2,3,2,0,2
283,4,2,0,4,3
284,3,2,1,4,1
285,3,0,3,4,4
286,2,4,0,4,3
287,1,4,2,3,2
288,1,0,2,2,3
289,2,0,0,1,1
290,4,2,3,3,4
291,1,3,0,0,0
292,4,1,0,3,2
293,2,3,3,2,1
294,0,3,1,4,3
295,4,2,0,0,1
296,1,3,1,4,3
297,2,3,2,4,2
298,0,0,4,2,1
299,3,0,0,0,0
300,4,2,3,0,1
301,1,3,4,0,3
302,2,0,0,3,1
303,1,0,0,2,0
304,1,4,3,2,3
305,0,3,2,4,3
306,2,4,1,3,2
307,4,2,2,2,4
308,3,0,0,1,0
309,2,1,4,3,3
310,2,1,4,4,3
311,3,4,3,3,3
312,3,2,4,3,4
313,2,3,2,4,1
314,2,1,4,0,0
315,3,4,3,3,3
316,0,2,2,0,0
317,2,4,1,1,3
318,1,2,3,2,2
319,2,2,0,1,0
320,1,3,3,3,3
321,4,3,3,3,3
322,4,1,0,2,4
323,4,2,0,2,3
324,0,0,3,4,1
325,3,2,2,1,1
326,3,1,0,0,0
327,0,3,3,4,2
328,2,0,0,1,1
329,0,0,0,2,0
330,2,0,1,3,4
331,0,0,2,2,0
332,0,0,2,1,0
333,0,0,0,1,2
334,3,0,4,2,4
335,4,1,1,3,2
336,4,2,3,4,1
337,4,0,4,0,0
338,0,2,3,2,1
339,3,3,1,4,1
340,3,4,4,0,3
341,0,2,2,0,4
342,3,3,4,1,4
343,4,1,2,3,2
344,3,0,0,0,1
345,2,3,0,1,0
346,3,0,1,0,4
347,2,1,1,4,0
348,1,1,2,2,4
349,4,4,1,4,4
350,1,0,0,2,3
351,0,1,4,1,4
352,2,3,4,2,0
353,1,4,3,0,4
354,0,2,4,4,4
355,0,4,4,1,4
356,2,4,2,0,3
357,0,1,3,1,1
358,2,1,4,2,3
359,0,2,2,0,0
360,2,4,1,4,4
361,4,4,4,1,4
362,1,1,1,4,4
363,2,4,2,2,0
364,4,0,1,3,0
365,4,0,3,3,3
366,3,4,4,4,3
367,1,3,2,0,1
368,0,2,4,3,4
369,1,0,4,3,1
370,2,0,1,3,0
371,3,1,0,1,2
372,1,4,4,4,4
373,3,1,1,1,1
374,0,2,4,3,0
375,4,3,0,0,1
376,4,3,1,2,1
377,3,4,1,1,1
378,0,3,4,3,2
379,4,3,0,2,2
380,3,3,0,4,0
381,2,4,1,2,1
382,4,3,1,4,4
383,1,2,2,4,2
384,4,0,3,4,2
385,0,1,2,2,1
386,2,0,1,0,0
387,2,2,1,4,2
388,1,1,3,4,1
389,4,1,4,4,1
390,3,3,1,2,1
391,1,0,2,2,3
392,4,0,1,4,4
393,2,3,1,4,3
394,4,3,2,0,0
395,1,2,1,3,1
396,1,2,4,1,1
397,1,0,4,0,3
398,0,3,4,2,4
399,3,1,2,0,1
400,2,4,1,0,4
401,4,2,4,4,1
402,2,2,4,1,4
403,2,2,4,4,2
404,4,3,1,3,3
405,1,0,3,0,3
406,1,4,2,3,2
407,2,4,3,2,4
408,1,1,1,1,1
409,2,0,3,0,1
410,2,0,1,0,4
411,3,1,2,2,4
412,3,2,2,3,4
413,4,4,2,0,3
414,4,4,1,4,1
415,0,4,0,0,0
416,3,0,2,2,2
417,0,4,0,3,4
418,0,1,0,2,3
419,2,0,4,1,0
420,3,3,0,3,0
421,2,3,0,1,0
422,2,1,4,3,1
423,1,2,0,1,3
424,2,2,2,2,3
425,4,0,0,3,0
426,2,2,0,4,2
427,0,3,0,2,2
428,2,2,2,3,0
429,2,3,1,4,1
430,4,0,3,3,0
431,1,1,1,4,4
432,1,2,3,2,2
433,3,4,0,4,2
434,2,2,2,4,0
435,4,1,3,4,0
436,2,3,3,0,2
437,2,3,4,3,3
438,1,4,2,0,1
439,2,3,3,4,0
440,1,0,3,0,4
441,1,3,1,1,3
442,3,4,3,4,1
443,2,0,2,0,3
444,2,3,3,4,2
445,3,0,2,4,4
446,4,0,0,2,1
447,4,1,1,4,3
448,1,1,0,3,1
449,1,0,1,3,3
450,0,0,3,4,3
451,0,1,1,0,1
452,4,3,1,0,0
453,1,1,2,4,1
454,3,1,3,4,0
455,0,0,2,1,0
456,1,0,0,1,4
457,2,3,0,0,2
458,2,4,4,3,0
459,1,4,4,2,2
460,0,0,1,2,2
461,3,2,1,0,2
462,1,4,4,1,4
463,0,0,1,1,2
464,0,4,2,1,0
465,0,4,0,1,4
466,1,4,3,3,0
467,4,0,0,0,4
468,2,4,1,0,1
469,4,4,3,4,0
470,4,4,4,2,2
471,3,1,4,0,4
472,1,4,3,1,1
473,2,0,3,4,1
474,0,2,2,1,3
475,3,2,1,0,0
476,0,4,3,3,0
477,2,2,4,4,0
478,1,4,4,1,0
479,0,2,0,3,0
480,2,3,1,3,4
481,4,1,2,2,1
482,1,0,1,0,3
483,1,2,3,0,0
484,2,1,1,3,0
485,4,4,3,2,4
486,2,1,4,4,0
487,3,0,0,2,0
488,1,1,4,3,3
489,0,0,2,3,3
490,0,3,4,3,1
491,0,1,4,4,3
492,0,3,1,3,1
493,1,4,3,0,0
494,0,2,2,0,3
495,2,1,3,2,1
496,1,4,4,4,3
497,1,4,1,3,0
498,1,4,4,2,0
499,3,0,4,2,4
500,3,1,3,2,1
501,2,2,1,2,4
502,4,4,2,3,4
503,4,2,3,0,4
504,1,2,0,4,2
505,0,4,0,1,3
506,3,4,1,0,3
507,3,1,0,1,4
508,4,2,0,3,3
509,4,4,1,2,2
510,3,0,4,1,4
511,1,0,3,0,3
512,3,1,1,4,2
513,3,3,3,0,3
514,2,0,4,2,1
515,0,1,0,1,3
516,0,0,1,3,1
517,1,2,2,3,1
518,4,3,0,3,3
519,0,4,4,4,0
520,2,4,0,1,0
521,4,4,0,1,0
522,3,4,3,0,1
523,3,4,2,4,1
524,3,1,3,3,1
525,0,4,3,2,3
526,1,2,0,0,0
527,4,4,3,2,2
528,1,0,0,0,4
529,1,3,1,2,4
530,4,3,4,3,0
531,4,0,4,4,2
532,1,3,3,4,2
533,2,3,3,2,1
534,3,1,1,3,0
535,0,1,2,2,4
536,0,4,4,4,4
537,3,3,1,0,0
538,3,2,4,4,4
539,3,0,0,2,1
540,1,0,1,1,3
541,0,2,3,2,0
542,0,4,2,4,1
543,0,4,3,1,0
544,3,4,4,4,2
545,2,0,0,1,4
546,4,3,1,1,3
547,2,2,4,0,4
548,1,1,0,2,0
549,0,0,2,3,1
550,1,3,2,4,3
551,1,4,1,2,3
552,4,0,1,0,0
553,4,4,1,2,3
554,2,4,3,3,4
555,1,4,4,2,3
556,1,3,4,1,3
557,3,1,3,2,1
558,3,3,4,1,3
559,2,1,1,1,3
560,1,3,4,1,4
561,3,4,2,0,0
562,2,1,1,3,1
563,3,0,4,3,0
564,0,0,1,0,1
565,1,2,3,2,3
566,1,0,2,3,1
567,4,1,0,4,1
568,3,0,1,1,1
569,2,4,4,4,2
570,4,4,0,2,0
571,2,2,4,4,1
572,3,1,1,3,2
573,3,0,1,0,1
574,0,2,4,3,1
575,1,2,3,2,4
576,3,3,1,3,3
577,0,0,2,3,2
578,0,0,3,0,1
579,2,1,1,3,4
580,2,4,2,0,4
581,2,2,2,0,3
582,1,1,4,1,3
583,4,3,1,2,3
584,4,3,1,4,2
585,0,0,2,1,0
586,1,2,1,3,1
587,0,4,4,4,1
588,4,2,1,0,4
589,0,0,1,1,4
590,0,0,4,3,1
591,0,2,4,0,2
592,2,4,0,1,3
593,3,2,0,1,1
594,0,1,4,2,4
595,3,1,4,0,1
596,0,0,2,0,0
597,4,3,2,1,4
598,1,0,2,3,1
599,4,1,0,4,3
600,4,0,4,2,3
601,3,2,2,4,4
602,2,4,3,2,3
603,4,1,1,0,3
604,0,4,1,2,0
605,4,1,4,4,2
606,3,2,0,4,0
607,0,1,3,2,1
608,2,1,2,1,3
609,3,1,2,3,1
610,0,3,2,4,0
611,3,1,3,0,1
612,0,0,2,3,1
613,2,2,0,3,1
614,2,0,4,2,1
615,2,0,4,4,3
616,3,4,1,2,3
617,0,4,4,0,2
618,1,1,4,4,4
619,1,0,3,3,1
620,1,3,2,1,0
621,0,2,4,4,0
622,4,2,0,1,1
623,1,2,0,2,4
624,4,2,2,2,0
625,3,2,1,2,0
626,1,1,4,4,4
627,0,4,1,1,4
628,0,1,3,3,0
629,2,0,3,1,4
630,0,0,1,4,4
631,1,0,0,4,4
632,0,0,3,0,1
633,1,0,1,0,1
634,3,1,4,0,1
635,2,1,1,3,1
636,2,2,2,1,2
637,4,2,1,4,0
638,2,4,3,4,1
639,1,0,3,0,2
640,0,1,3,0,0
641,0,3,0,2,4
642,3,4,3,3,0
643,3,0,4,4,3
644,3,1,0,0,0
645,1,3,2,4,4
646,3,0,1,4,1
647,3,0,4,0,2
648,4,1,2,4,3
649,0,2,0,3,0
650,3,0,2,0,2
651,0,4,0,0,2
652,3,2,1,1,4
653,0,3,4,2,1
654,3,1,1,4,4
655,3,3,3,0,0
656,1,4,4,0,0
657,3,3,0,0,2
658,2,3,0,1,2
659,1,4,2,0,0
660,3,3,3,3,1
661,3,2,3,3,3
662,0,4,1,4,2
663,2,0,0,0,1
664,1,2,4,2,0
665,1,2,4,4,1
666,1,1,3,2,2
667,0,0,2,1,2
668,2,4,2,1,1
669,0,2,0,0,0
670,1,0,1,4,2
671,1,0,4,2,1
672,3,1,3,2,3
673,3,3,0,3,1
674,3,3,4,4,1
675,4,2,4,0,0
676,3,2,4,0,4
677,0,2,2,1,4
678,4,1,1,4,3
679,1,1,3,2,3
680,0,1,0,2,1
681,0,4,1,2,2
682,0,1,2,1,1
683,0,4,2,1,0
684,1,4,3,4,1
685,3,4,4,4,1
686,2,0,4,0,0
687,1,1,4,0,0
688,1,1,0,4,0
689,2,1,1,3,0
690,2,0,3,0,1
691,1,1,1,2,3
692,4,3,2,2,1
693,0,2,4,4,2
694,4,0,0,1,1
695,4,0,2,4,0
696,2,2,1,4,2
697,3,0,2,4,2
698,1,2,0,2,3
699,3,0,1,2,3
700,1,1,2,0,1
701,2,2,0,4,4
702,3,1,4,4,3
703,3,4,0,0,3
704,3,3,4,0,1
705,4,3,3,2,3
706,4,4,3,4,4
707,2,0,0,4,1
708,0,1,4,1,0
709,3,1,2,3,1
710,2,4,2,0,3
711,4,2,4,0,3
712,0,0,2,4,2
713,2,4,4,0,2
714,3,2,4,4,3
715,1,0,1,2,4
716,1,3,2,2,0
717,1,2,2,4,0
718,0,3,3,3,4
719,3,3,2,3,0
720,0,1,3,4,0
721,4,4,1,1,0
722,4,0,4,3,3
723,2,3,1,1,2
724,3,1,2,3,0
725,4,3,2,3,4
726,0,1,4,2,2
727,2,0,0,1,4
728,4,2,0,1,3
729,2,3,2,2,3
730,0,3,1,4,0
731,3,0,3,3,1
732,3,0,4,3,2
733,2,3,4,2,1
734,1,2,2,4,3
735,2,2,0,0,1
736,4,0,4,2,1
737,0,2,2,3,0
738,1,0,1,3,3
739,2,4,2,1,4
740,1,1,1,4,0
741,0,2,1,2,3
742,3,3,4,1,3
743,3,2,0,4,0
744,1,2,3,1,2
745,1,4,0,2,3
746,4,2,3,4,3
747,1,2,0,3,4
748,1,3,2,1,4
749,4,1,3,4,4
750,0,1,1,1,2
751,1,0,1,4,3
752,1,3,3,2,4
753,3,0,4,1,2
754,0,2,1,4,2
755,2,1,2,1,0
756,2,3,1,3,3
757,3,0,0,2,1
758,1,1,4,0,4
759,3,2,2,1,2
760,0,1,0,1,4
761,0,2,2,0,3
762,0,0,1,2,4
763,0,3,4,3,4
764,4,3,3,1,0
765,2,3,4,2,0
766,0,4,1,2,2
767,2,1,1,1,1
768,3,1,4,0,2
769,4,4,4,3,1
770,4,0,2,2,3
771,0,4,3,4,4
772,3,2,4,3,1
773,4,4,1,3,0
774,0,0,3,0,0
775,3,0,3,0,3
776,2,0,0,0,3
777,1,1,1,3,4
778,4,1,3,4,2
779,3,1,4,3,1
780,3,2,4,0,0
781,2,0,3,4,3
782,2,3,0,2,0
783,3,2,4,3,1
784,0,3,1,0,0
785,0,2,3,2,2
786,4,2,1,3,4
787,4,3,2,0,3
788,1,3,3,3,0
789,4,4,0,1,3
790,0,0,2,2,3
791,3,2,3,3,1
792,4,4,3,4,3
793,4,4,1,2,1
794,3,2,0,3,3
795,1,0,4,3,3
796,1,3,4,4,2
797,2,1,4,1,2
798,2,0,1,2,0
799,0,2,1,1,1
800,3,2,3,0,4
801,1,0,2,1,3
802,0,0,2,0,1
803,3,0,0,4,1
804,4,1,3,4,4
805,1,3,0,4,3
806,4,3,1,4,3
807,1,4,1,4,3
808,4,1,1,1,3
809,3,1,3,3,2
810,0,3,3,0,3
811,4,0,4,0,2
812,3,2,1,4,0
813,3,4,1,0,0
814,3,3,0,4,4
815,3,1,3,0,3
816,0,4,0,0,3
817,1,2,3,1,4
818,2,0,3,0,2
819,3,1,3,3,3
820,1,2,3,0,3
821,3,4,4,1,1
822,3,1,4,4,2
823,1,3,3,3,2
824,1,0,3,3,2
825,1,1,4,3,4
826,0,4,2,2,2
827,3,3,2,2,4
828,3,3,4,2,3
829,2,0,0,2,1
830,1,0,2,4,1
831,0,3,1,3,0
832,2,1,3,1,2
833,2,4,1,4,3
834,0,4,0,0,0
835,4,1,2,0,0
836,0,4,0,0,4
837,2,2,0,2,0
838,1,1,1,2,2
839,1,1,3,2,4
840,0,0,0,1,4
841,0,4,0,0,3
842,3,3,3,0,1
843,4,4,0,0,1
844,0,2,1,2,2
845,2,3,4,3,2
846,3,1,0,0,1
847,0,2,1,2,1
848,1,2,3,2,3
849,1,4,3,4,2
850,3,2,4,3,1
851,2,0,1,3,3
852,4,4,0,3,1
853,4,3,1,4,3
854,2,4,4,4,4
855,0,4,3,4,0
856,0,2,1,0,0
857,3,1,4,3,1
858,3,2,0,4,4
859,0,2,2,3,2
860,4,3,0,2,1
861,0,0,3,1,3
862,0,2,2,3,0
863,1,0,2,3,3
864,2,0,2,1,2
865,0,2,4,0,4
866,3,4,1,2,2
867,3,4,1,1,1
868,4,4,3,0,2
869,0,2,4,1,4
870,3,3,3,4,1
871,1,0,3,1,4
872,0,4,1,4,3
873,2,1,3,1,3
874,4,1,1,4,4
875,1,0,2,0,3
876,1,0,1,4,3
877,4,1,0,4,3
878,2,0,0,4,1
879,0,1,0,1,3
880,3,2,3,2,4
881,3,4,4,4,2
882,4,0,4,0,3
883,4,1,1,4,3
884,4,4,1,2,1
885,4,4,2,2,0
886,0,0,3,2,1
887,4,1,0,1,0
888,1,3,2,4,0
889,3,2,3,4,1
890,1,0,0,4,2
891,1,0,3,4,2
892,3,3,2,4,1
893,0,4,1,1,4
894,0,0,0,2,4
895,0,0,0,3,4
896,2,4,3,3,3
897,1,4,0,2,2
898,3,3,1,3,0
899,3,1,0,4,3
900,0,4,3,0,0
901,1,4,3,0,3
902,4,1,2,3,3
903,0,1,3,4,1
904,2,4,4,4,1
905,3,2,3,2,2
906,3,4,0,0,3
907,1,3,0,4,1
908,1,4,1,3,4
909,1,4,0,0,2
910,1,2,0,3,2
911,4,1,0,0,0
912,4,3,1,3,3
913,0,1,0,1,4
914,0,3,4,2,2
915,4,1,3,4,0
916,2,3,3,4,3
917,2,1,1,2,2
918,1,2,0,2,4
919,1,1,4,1,4
920,3,2,4,1,0
921,4,0,3,3,2
922,3,3,0,4,1
923,2,0,1,3,2
924,0,4,3,2,1
925,1,2,0,4,4
926,3,3,2,3,4
927,4,2,0,2,1
928,3,0,2,4,0
929,1,2,1,1,2
930,4,4,0,2,4
931,4,2,2,3,2
932,0,3,4,1,1
933,0,1,3,4,0
934,1,3,4,1,0
935,0,1,1,0,3
936,2,2,3,4,2
937,2,4,0,1,0
938,1,2,0,4,1
939,1,0,3,3,2
940,1,4,4,0,1
941,0,3,3,4,0
942,2,2,3,2,1
943,2,3,3,3,4
944,2,4,4,3,4
945,0,2,0,2,0
946,0,4,0,3,4
947,2,4,3,2,0
948,1,4,1,1,3
949,4,3,4,2,0
950,3,4,0,1,0
951,0,0,2,3,4
952,4,1,0,1,2
953,2,3,3,4,4
954,2,4,1,1,1
955,4,3,3,3,3
956,0,3,3,4,0
957,2,4,2,4,2
958,4,1,3,3,1
959,4,3,1,1,3
960,1,3,3,2,4
961,1,3,4,2,3
962,1,3,4,1,1
963,2,4,0,2,2
964,0,0,3,1,2
965,1,4,2,2,3
966,4,2,1,3,2
967,0,0,2,2,0
968,3,1,0,1,2
969,2,1,0,0,0
970,1,0,4,1,3
971,2,0,4,1,1
972,4,3,1,1,0
973,4,1,0,4,4
974,1,2,0,4,0
975,2,1,0,4,1
976,3,0,2,1,2
977,1,2,4,2,1
978,1,4,3,3,0
979,1,2,0,0,1
980,4,4,1,4,0
981,4,4,0,1,4
982,3,3,3,4,2
983,4,4,1,4,2
984,2,0,4,2,4
985,2,1,0,4,0
986,4,4,4,3,4
987,4,1,1,2,4
988,2,1,4,4,2
989,2,3,4,1,1
990,1,3,1,3,0
991,2,1,3,2,2
992,1,0,4,2,2
993,0,0,1,3,0
994,3,3,2,3,1
995,2,3,3,4,2
996,3,2,3,2,4
997,4,0,2,0,1
998,1,4,0,0,0
999,3,3,3,4,4
'''

a = a.split('\n')
a =[i.split(',') for i in a]

code = {1:'a',2:'b',3:'c',4:'d'}

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def unicity_calculator(a):

    power_set = list(powerset([1,2,3,4]))


    final_ans = {}
    for i in power_set:
        alphabet = [code[j] for j in i]
        freq_tracker = {}
        for values in a:
            key_val = ''
            for indexes in i:
                key_val += values[indexes]
            if key_val not in freq_tracker:
                freq_tracker[key_val] = 1
            else:
                freq_tracker[key_val] += 1
#         print freq_tracker

        for k in freq_tracker:
            if freq_tracker[k] == 1:
                index_key = ''.join(alphabet)
                if index_key not in final_ans:
                    final_ans[index_key] = [k]
                else:
                    final_ans[index_key].append(k)

    for j in final_ans:
        print j
        for val in final_ans[j]:
            print val

        print "---------------"




unicity_calculator(a)

# for j in ans:
#     if ans[j] == 1:
#         print j, ans[j]
