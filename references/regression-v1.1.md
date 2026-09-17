# V1.1 Regression Guidance

Read this file only when maintaining or evaluating the Skill. It is not part of normal image-to-floral runtime context.

## Order

Run the old images before any new-image evaluation:

1. Bad-case regression: TEST-02, TEST-03, TEST-05, TEST-08, TEST-09.
2. Protected positive benchmarks: TEST-04 and TEST-06.

Use the normal fixed decoder chain and generate one candidate per bad-case test. Score the candidate against the same 100-point rubric used for V1; compare against the saved V1 score when available. If a hard output constraint fails, the normal single focused correction remains allowed for bad cases.

## Bad-case targets

- TEST-02: the pale-blue environment receives a visible carrier.
- TEST-03: pale and mid-blue tonal layers remain distinct instead of collapsing into deep blue.
- TEST-05: pink paper stays opaque, matte, structured, and planar; handwritten rhythm may appear locally on its assigned carrier.
- TEST-08: motion reads downward and centripetal through internal cascading topology toward `lower_center`, never upward or radial-outward. Keep the base/tie below the floral body; do not force an inverted, top-tied, broom-like, or tassel-like presentation merely to show falling.
- TEST-09: low-area, high-attention red becomes one unmistakable Hero plus at most one or two supports.

The five-case mean must improve by at least four points over V1 without introducing semantic error, literal copy, template regression, output-constraint failure, or a non-white background.

## Protected no-correction benchmarks

TEST-04 and TEST-06 are absolute no-correction benchmarks. Do not generate or regenerate them during V1.1 patch evaluation. Freeze and inspect the saved V1 baseline outputs as immutable references, and audit the new rules against the strengths they protect. Generate a new version only when the user explicitly requests one. Any newly generated candidate is not a benchmark and must not replace the saved baseline.

- TEST-04 baseline: 92/100. Protect semi-transparent enclosure, carrier assignment, and black-white-gray material relations. The candidate must score at least 90.
- TEST-06 baseline: 93/100. Protect palette purity, complete environment color, warm-yellow childlike mood, and non-literal translation. The candidate must score at least 91.

Fixture pairs are stored under `assets/benchmarks/v1.1/test-04/` and `assets/benchmarks/v1.1/test-06/`. `reference.jpg` is the decoder input; `v1-baseline.png` is the accepted V1 output for visual comparison. Do not load these fixtures during normal tasks or use either baseline output as an image-generation reference.
