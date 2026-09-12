# Ultrawide Fog Tint Fix (CK3)

Removes the warm haze that washes out the left side of the map on ultrawide and
super-ultrawide displays. Ordinary distance fog is left alone.

## Cause

`jomini_fog.fxh` blends a second fog colour on top of the normal one, and the
blend factor depends on nothing but how far **left of the camera** a pixel is:

    float BlendFactor = smoothstep( CameraPosition.x + RelativeFogBegin,
                                    CameraPosition.x - RelativeFogEnd,
                                    WorldSpacePos.x );
    float3 BlendedFogColor = FogColor + BlendFactor * RelativeFogColor;

With the vanilla values from `gfx/map/environment/environment.txt`:

    relative_fog_color = { 0.6 0.2 -0.2 }
    relative_fog_begin = 100.0
    relative_fog_end   = 400.0

the gradient runs out over a 500 unit window either side of the camera, and
`RelativeFogColor` adds a lot of red, some green and *subtracts* blue - a warm,
desaturating wash.

On 16:9 that window is about as wide as the visible map, so the effect reads as a
gentle atmospheric gradient. On 32:9 the screen is roughly twice as wide in world
units, so everything past 400 units to the left sits at blend factor 1 and takes
the full tint: the left third of the map goes pale and the conifers there turn
almost white, while the same trees in the centre look normal.

It is the same class of bug as the pause menu one - a value tuned for a 16:9 field
of view, applied unscaled to a much wider one.

## Fix

`relative_fog_color` is set to `{ 0 0 0 }` in the five environment files that
carry a non-zero value:

    environment.txt
    environment_top_left.txt
    environment_bottom_left.txt
    environment_ce2.txt
    environment_compromise.txt

(the `*_table` environments already ship it zeroed). The blend factor still gets
computed, it just adds nothing.

Everything else is untouched: `fog_color`, `fog_begin`, `fog_end` and `fog_max`
still give the normal blue distance haze, and `relative_fog_height_begin/end`
still fade fog out with altitude.

## Softening it instead of removing it

If you would rather keep the effect but have it behave the way it does on 16:9,
leave `relative_fog_color` alone and widen the window instead - scale both
distances by roughly your aspect ratio over 16:9. For 5120x1440 that is
`3.56 / 1.78 = 2`:

    relative_fog_begin = 200.0
    relative_fog_end   = 800.0

The gradient then spans twice the world distance, so a given screen position gets
about the tint a 16:9 player sees there.

## Layout

    descriptor.mod                       mod metadata
    gfx/map/environment/*.txt            five environment files, relative fog zeroed
    install.sh                           copies the mod into the Proton prefix

## Installing

Run `./install.sh`, then enable "Ultrawide Fog Tint Fix" in the launcher playset.
No shader is touched, so there is no shader recompile and no first-load delay -
and toggling the mod in the playset is a clean A/B test.

## Game version

Built against 1.19.0.6 (Scribe). These files are full overrides, so after a patch
re-diff them against `<steam>/Crusader Kings III/game/gfx/map/environment/`.

## Compatibility

Conflicts with mods that replace the same environment files - map graphics or
lighting overhauls. Load this one below them to keep the fix.
