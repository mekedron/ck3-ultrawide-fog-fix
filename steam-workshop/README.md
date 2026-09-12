# Steam Workshop publishing kit

Everything needed for the Steam Workshop and Paradox Mods listings. Nothing here ships with the
mod itself — the mod is `descriptor.mod`, `thumbnail.png` and `gfx/` in the repository root.

| File | Where it goes |
| --- | --- |
| `description-en.txt` | Workshop item description (BBCode) |
| `description-ru.txt` | Russian version of the same description |
| `description-paradoxmods-en.txt` | same text without BBCode, for the Paradox Mods site |
| `description-paradoxmods-ru.txt` | Russian version without BBCode |
| `short-description-en.txt` | Launcher / Paradox Mods short description, 196 chars |
| `short-description-ru.txt` | Russian short description, 182 chars |

The `description-paradoxmods-*.txt` files are mechanically derived from the BBCode ones
(headers uppercased, `[*]` to `-`, tags dropped, `[url]` reduced to the bare link). Edit the
BBCode version first, then regenerate, so the two never drift apart.

## Listing metadata

* **Title:** Ultrawide Fog Tint Fix
* **Tags:** Fixes, Graphics, Utilities — same as `descriptor.mod`
* **Version:** 1.0.0, `supported_version="1.19.*"`
* **Visibility:** public

Short descriptions are kept under the launcher's 200 character limit; both BBCode descriptions
are well under Steam's 8000 character limit.

## Which preset to publish

The item ships whatever `tools/apply_preset.py` last wrote into `gfx/map/environment/`. Check
before uploading:

    head -1 gfx/map/environment/environment.txt

The published item is meant to be the **off** preset - it is the one that answers the complaint
people will arrive with. The description lists the other four and points at the repository for
them.

## Preview image on Steam

The Workshop preview is **not** set from the uploader form — the launcher picks up
`thumbnail.png` from the mod root (next to `descriptor.mod`), which is also what
`picture="thumbnail.png"` in the descriptor points at. Without that file the item shows Steam's
default placeholder, and images added to the item's gallery on the website do not replace it.

`thumbnail.png` is 1280x1280, 658 KB, under Steam's 1 MB preview limit, quantised to a 256
colour palette and rebuilt from raw pixels so it carries no metadata. `tools/make_thumbnail.py`
regenerates it from two screenshots.

Note the two screenshots it is built from are not pixel-identical framings - the camera moved
slightly between them. That is fine here because the bug is visible *within* the top frame on
its own: the same bay is brown on the left and blue on the right. If you want a strict pair,
take two shots from one camera position with the mod toggled in the playset and re-run the
generator.

## Screenshots for the item gallery

1. the before/after pair the thumbnail is built from, full width
2. a northern forest, where the white-conifer effect is most obvious
3. optional: the same view with the `soft` preset, to show the middle ground
