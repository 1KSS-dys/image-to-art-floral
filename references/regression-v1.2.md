# V1.2 Carrier Preservation Regression

This maintenance-only regression protects Carrier Assignment from V1.2 Material Casting. It is not part of normal runtime context and must not become a reusable composition template.

## CASE03 — black editorial sea translation

Reference fixture: `../assets/regression/v1.2/case03-reference.jpg`

Validated hotfix output: `../assets/regression/v1.2/case03-hotfix-output.png`

The source is decoded without retrieving a case. Preserve these locked assignments:

| Visual information | Priority | Locked carrier | Permitted material scope | Required result |
|---|---|---|---|---|
| black editorial environment | Level 1 | backboard | paper / cardstock / rigid sheet | large matte-black planar field |
| pale-blue sky tonality | Level 1 | wrapper | packaging / wrapper | pale-blue translucent layer |
| mid-blue transition | Level 1 | wrapper | packaging / wrapper | distinct medium-blue translucent layer |
| deep-blue ocean tonality | Level 1 | wrapper | packaging / wrapper | deep-blue layered film or wrap |
| cyan handwriting and flowing lines | Level 1 / important Level 2 | typography / linear material on its assigned carrier | printed or handmade marks on paper; thin line material | cyan stroke rhythm without reconstructing full wording |
| tiny warm subject | important Level 2 | flower | flower library | one very small warm-yellow floral accent |

The focus architecture is `environment_dominant`; a singular Hero is not required. Packaging and backboard must remain the largest visual area. Use only a small amount of botanical material, sufficient to preserve an intentional floral organization.

### Required prohibitions

- no giant black foliage replacing the matte-black paper or backboard;
- no mass of blue flowers replacing pale-, mid-, or deep-blue wrapper layers;
- no photographic or illustrated sea, sky, horizon, cloud, or person printed, pasted, projected, or screened on any carrier;
- no disappearing or visually negligible wrapper;
- no cross-category Carrier substitution unless the upstream Decoder explicitly set `carrier_override_allowed: true` before Bouquet Structure.

### Pass criteria

- all locked Level 1 carriers are visibly present in the final prompt and image;
- matte-black paper/backboard plus three distinguishable blue packaging layers carry the environment;
- cyan handwriting-like marks or thin lines remain abstract visual texture;
- the warm floral accent remains tiny relative to the packaging system;
- the result is exactly one complete floral arrangement on pure white, with no environment scene or reference-image reproduction;
- `carrier_preservation_qa` passes without recasting or re-decoding.
