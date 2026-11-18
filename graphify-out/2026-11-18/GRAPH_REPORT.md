# Graph Report - unchainedlife-app  (2026-11-07)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1886 nodes · 4567 edges · 96 communities (88 shown, 8 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.85)
- Token cost: 52,280 input · 1,211 output

## Graph Freshness
- Built from commit: `cfbe6b39`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Film Build Tools
- Plugin CLI Entrypoint
- Sound Family Matching
- Loudness Measurement
- Cue Folding Config
- Sound Catalog Index
- Ambience Bed Generation
- HeyGen Voice Scripts
- Text and Path Utilities
- Candidate Contact Sheets
- UI Event Detection
- Mixer Processing
- Quality Assurance Checks
- Unbake Layer Fitting
- Moment Testing
- Lyria BGM Generation
- Master Bus Limiting
- Beat Grid Detection
- Audio Metadata CLI
- TTS Provider Selection
- Source Carving
- Openverse SFX Search
- Config and Telemetry
- Recipe Store
- Style Learning Analysis
- Synth Event Extraction
- Masking Analysis
- Reference Style Comparison
- Review and Packaging
- Dither Image Processing
- Video Moment Finding
- Preferences Store
- Licence Audit
- JS Project Config
- Media Manifest
- HyperFrames Import
- Visual Inspection Sheets
- BGM Retrieval
- BGM Wait Polling
- Tonal Feature Analysis
- TypeScript App Config
- Level Comparison
- Cut List Compilation
- Transcription and Npx
- Sound Captioning Model
- Gemini Auth and Python
- Audio Video Muxing
- TypeScript Node Config
- Gemini Auth Tests
- Audio Ducking
- Transcript Cut Fades
- Audio File Analysis
- Dev Dependencies
- Evaluation Reports
- Music Arrangement
- Locate and Grid Filters
- Audio Data Extraction
- Landing Page Components
- SFX Tests
- Licence Classification
- React App Entry
- HyperFrames Config
- Basemap Baking
- Media Record Tests
- Credits Generation
- Speech Pause Map
- Index Generation
- Band Metrics
- Loudness Input Errors
- NPM Scripts
- Chime Sound Manifest
- App Dependencies
- Click Sound Manifest
- Click-Soft Sound Manifest
- Error Sound Manifest
- Glitch 1 Manifest
- Glitch 2 Manifest
- Glitch 3 Manifest
- Impact Bass 1 Manifest
- Impact Bass 2 Manifest
- Key Press Manifest
- Notification Sound Manifest
- Ping Sound Manifest
- Pop Sound Manifest
- Riser Sound Manifest
- Sparkle Sound Manifest
- Typing Sound Manifest
- Whoosh Manifest
- Cinematic Whoosh Manifest
- Short Whoosh Manifest
- Social Proof Component
- Supabase Client
- TypeScript Project References

## God Nodes (most connected - your core abstractions)
1. `main()` - 53 edges
2. `main()` - 43 edges
3. `load_json()` - 34 edges
4. `load_index()` - 34 edges
5. `run()` - 26 edges
6. `main()` - 25 edges
7. `rank()` - 25 edges
8. `load_config()` - 24 edges
9. `unbake()` - 22 edges
10. `effective_dur()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `bundledOnly()` --calls--> `resolveSfx()`  [EXTRACTED]
  .claude/skills/media-use/audio/scripts/lib/sfx.test.mjs → .claude/skills/media-use/audio/scripts/lib/sfx.mjs
- `run()` --calls--> `resolveSfx()`  [EXTRACTED]
  .claude/skills/media-use/audio/scripts/lib/sfx.test.mjs → .claude/skills/media-use/audio/scripts/lib/sfx.mjs
- `record()` --calls--> `appendRecord()`  [EXTRACTED]
  .claude/skills/media-use/audio/scripts/lib/sfx.test.mjs → .claude/skills/media-use/scripts/lib/manifest.mjs
- `build_layers()` --calls--> `Lib`  [EXTRACTED]
  .claude/skills/real-sound/scripts/qa.py → .claude/skills/real-sound/scripts/mix.py
- `check_edges()` --calls--> `Lib`  [EXTRACTED]
  .claude/skills/real-sound/scripts/qa.py → .claude/skills/real-sound/scripts/mix.py

## Import Cycles
- None detected.

## Communities (96 total, 8 thin omitted)

### Community 0 - "Film Build Tools"
Cohesion: 0.05
Nodes (44): build_film(), put_stem(), cmd_build(), cmd_ladder(), db(), duck_stem(), excerpt(), ff() (+36 more)

### Community 1 - "Plugin CLI Entrypoint"
Cohesion: 0.06
Nodes (29): isMainModule(), CLI_MEDIA_USE, SKILLS, skillScripts(), invocation(), manifests, pluginVersion(), root (+21 more)

### Community 2 - "Sound Family Matching"
Cohesion: 0.05
Nodes (36): centroid_window(), family_key(), anchors_map(), assign_onsets(), baked_layer(), canon(), clean_pool(), detect_typing_runs() (+28 more)

### Community 3 - "Loudness Measurement"
Cohesion: 0.05
Nodes (37): arrive_offset(), channel_count(), clean_hits(), measure_loudness(), grab(), mono_drop(), onsets(), show_name() (+29 more)

### Community 4 - "Cue Folding Config"
Cohesion: 0.06
Nodes (30): arrival_landmarks(), decode_mono(), decode_sound(), events_track(), _fold(), fold_cues(), fold_report(), index_path() (+22 more)

### Community 5 - "Sound Catalog Index"
Cohesion: 0.08
Nodes (30): _catalog_key(), describe(), load_catalog(), main(), _num(), pack_record(), _read_catalog(), scan() (+22 more)

### Community 6 - "Ambience Bed Generation"
Cohesion: 0.08
Nodes (31): proj(), authenticate(), candidates(), main(), pieces(), scan(), tags_of(), usable() (+23 more)

### Community 7 - "HeyGen Voice Scripts"
Cohesion: 0.07
Nodes (34): argv, dur, output, positional, clone(), list(), main(), MEDIA_TYPES (+26 more)

### Community 8 - "Text and Path Utilities"
Cohesion: 0.08
Nodes (30): _decode_text(), gesture_times(), load_json(), norm_path(), read_stdin_text(), read_text_any(), abspath(), apply_batch() (+22 more)

### Community 9 - "Candidate Contact Sheets"
Cohesion: 0.10
Nodes (26): effective_dur(), require_tools(), esc(), find_font(), main(), one_row(), render_sheet(), bank_from_ids() (+18 more)

### Community 10 - "UI Event Detection"
Cohesion: 0.07
Nodes (21): analyse(), checkpoints_picture(), draw_timeline(), drop_periodic(), grid_results(), _in_range(), main(), native_windows() (+13 more)

### Community 11 - "Mixer Processing"
Cohesion: 0.11
Nodes (23): apply_fades(), auto_curve(), biquad(), check_files(), db2a(), decode(), dump(), env_index() (+15 more)

### Community 12 - "Quality Assurance Checks"
Cohesion: 0.09
Nodes (30): build_layers(), centroid(), check_audibility(), check_clicks(), check_coverage(), check_density(), check_edges(), check_harshness() (+22 more)

### Community 13 - "Unbake Layer Fitting"
Cohesion: 0.11
Nodes (24): _best_lag(), classify(), coarse_lag(), _corr(), _decode(), _decode_sum(), _dot(), _duration() (+16 more)

### Community 14 - "Moment Testing"
Cohesion: 0.08
Nodes (22): build_moment(), candidates_for(), cmd_build(), current_cues(), _ir(), kpower(), loud150(), lufs_of() (+14 more)

### Community 15 - "Lyria BGM Generation"
Cohesion: 0.10
Nodes (20): generate_bgm(), main(), parse_args(), analyse(), ath_power(), band_power(), bark(), decode() (+12 more)

### Community 16 - "Master Bus Limiting"
Cohesion: 0.13
Nodes (19): blocks(), bus_comp(), edge_fades(), finish(), gate(), glue(), integrated(), _kw() (+11 more)

### Community 17 - "Beat Grid Detection"
Cohesion: 0.09
Nodes (17): beat_grid(), check_grid(), decode(), detect(), detrend(), kick_peaks(), kick_phase_shift(), kick_stats() (+9 more)

### Community 18 - "Audio Metadata CLI"
Cohesion: 0.07
Nodes (24): anomalies, argv, audioMeta, bgmFields, bgmModeOverride, HERE, hyperframesDir, langOverride (+16 more)

### Community 19 - "TTS Provider Selection"
Cohesion: 0.12
Nodes (24): heygenMessage(), elevenlabsAvailable(), ffmpegDurationFallback(), ffprobeDuration(), heygenAvailable(), parseFfmpegDurationBanner(), pickProvider(), relTo() (+16 more)

### Community 20 - "Source Carving"
Cohesion: 0.20
Nodes (16): attrOf(), carveSources(), decode(), DEFAULT_STRENGTH, detectTracks(), escapeAttr(), fail(), groupSourceRefusal() (+8 more)

### Community 21 - "Openverse SFX Search"
Cohesion: 0.20
Nodes (21): downloadTo(), agentWritePath(), httpsUrl(), oneLine(), OPENVERSE_SFX_LICENSES, OpenverseUnavailableError, penalty(), pickOpenverseSfx() (+13 more)

### Community 22 - "Config and Telemetry"
Cohesion: 0.18
Nodes (19): withFileLock(), globalMediaDir(), mediaHome(), anonymousId(), __anonymousIdForTest(), heygenAccount(), heygenUserId(), identifyAccount() (+11 more)

### Community 23 - "Recipe Store"
Cohesion: 0.18
Nodes (21): nextId(), BRIEF_CONTENT_KEYS, briefWorkflow(), FRAME_CONTENT_KEYS, frameTitle(), freezeRecipe(), FRONTMATTER_CONTENT_KEYS, listRecipes() (+13 more)

### Community 24 - "Style Learning Analysis"
Cohesion: 0.14
Nodes (13): avg_power(), character_from_power(), added_character(), aggregate(), analyse(), audio_events(), band_db(), decode() (+5 more)

### Community 25 - "Synth Event Extraction"
Cohesion: 0.14
Nodes (14): _balanced(), extract(), find_functions(), find_scripts(), from_objects(), instrument(), main(), _project_dir() (+6 more)

### Community 26 - "Masking Analysis"
Cohesion: 0.13
Nodes (11): active_level_diff(), band_env(), cue_levels(), full_env(), lowend_collisions(), main(), masked_cues(), speech_active() (+3 more)

### Community 27 - "Reference Style Comparison"
Cohesion: 0.13
Nodes (12): aggregate(), _band(), bed_share(), compare(), export(), find_style(), gestures(), group_gestures() (+4 more)

### Community 28 - "Review and Packaging"
Cohesion: 0.14
Nodes (9): main(), ff(), main(), render(), main(), ui_cue(), ff(), has_audio() (+1 more)

### Community 29 - "Dither Image Processing"
Cohesion: 0.18
Nodes (19): frameRateNumber(), IMAGE_EXTENSIONS, OUTPUT_IMAGE_EXTENSIONS, probe(), processImage(), processVideo(), run(), temporaryOutput() (+11 more)

### Community 30 - "Video Moment Finding"
Cohesion: 0.19
Nodes (14): run(), audio_level(), detect(), diff_series(), main(), refine(), scene_cuts(), series_peaks() (+6 more)

### Community 31 - "Preferences Store"
Cohesion: 0.20
Nodes (17): dedupe(), emptyFile(), isRecord(), mergedPreferences(), PREFERENCE_KEYS, preferenceKeyFor(), projectPrefsPath(), PROMOTE_AT (+9 more)

### Community 32 - "Licence Audit"
Cohesion: 0.15
Nodes (12): agent_fields(), audit(), audit_entry(), backup(), decodes_clean(), fetch_match(), ffprobe(), main() (+4 more)

### Community 33 - "JS Project Config"
Cohesion: 0.12
Nodes (18): name, private, type, version, autoprefixer, eslint, @eslint/js, eslint-plugin-react-hooks (+10 more)

### Community 34 - "Media Manifest"
Cohesion: 0.23
Nodes (19): allocateId(), appendRecord(), findByPrompt(), manifestPath(), mediaDir(), nextFreeId(), normalizePrompt(), readManifest() (+11 more)

### Community 35 - "HyperFrames Import"
Cohesion: 0.15
Nodes (9): Collector, find_calls(), hint_of(), load(), resolve(), num(), split_args(), strength_of() (+1 more)

### Community 36 - "Visual Inspection Sheets"
Cohesion: 0.25
Nodes (13): at(), esc(), events_sheet(), ff(), find_font(), frames_row(), label_filter(), main() (+5 more)

### Community 37 - "BGM Retrieval"
Cohesion: 0.22
Nodes (14): BGM_PY_DEPS, generateBgmDetached(), inferBgmPrompt(), LYRIA_PY_DEPS, lyriaKey(), musicgenScript(), pipInstall(), pyOk() (+6 more)

### Community 38 - "BGM Wait Polling"
Cohesion: 0.11
Nodes (10): argv, audioMeta, audioMetaPath, base, hyperframesDir, intervalMs, outPath, started (+2 more)

### Community 39 - "Tonal Feature Analysis"
Cohesion: 0.21
Nodes (10): _fft(), sound_features(), best_shift(), chroma(), _decode(), _mags(), main(), midi_name() (+2 more)

### Community 40 - "TypeScript App Config"
Cohesion: 0.11
Nodes (17): compilerOptions, allowImportingTsExtensions, isolatedModules, jsx, lib, module, moduleDetection, moduleResolution (+9 more)

### Community 41 - "Level Comparison"
Cohesion: 0.17
Nodes (7): combine(), compare(), edits(), groups(), level_in(), main(), momentary()

### Community 42 - "Cut List Compilation"
Cohesion: 0.25
Nodes (16): bareToken(), clampRanges(), cleanRange(), compileCutList(), durationFrom(), fillerRanges(), finalizeKept(), hasRemovalSource() (+8 more)

### Community 43 - "Transcription and Npx"
Cohesion: 0.18
Nodes (12): resolveNpxCliPath(), resolveNpxInvocation(), mergeTokensToWords(), dist, root, atomicWrite(), inputPath, outPath (+4 more)

### Community 44 - "Sound Captioning Model"
Cohesion: 0.25
Nodes (11): ask_model(), bench(), bench_captions(), ffmpeg(), have_model(), install(), main(), run_jobs() (+3 more)

### Community 45 - "Gemini Auth and Python"
Cohesion: 0.23
Nodes (7): geminiAuth(), geminiConfigured(), defaultProbe(), pythonCommand(), pythonInvocation(), resolvePythonCommand(), posixOnly

### Community 46 - "Audio Video Muxing"
Cohesion: 0.13
Nodes (12): abr, args, argv, audio, fail(), out, pa, po (+4 more)

### Community 47 - "TypeScript Node Config"
Cohesion: 0.12
Nodes (15): compilerOptions, allowImportingTsExtensions, isolatedModules, lib, module, moduleDetection, moduleResolution, noEmit (+7 more)

### Community 49 - "Audio Ducking"
Cohesion: 0.30
Nodes (12): escapeRegExp(), readTargetAttrs(), run(), { values: args }, duckKeyframes(), duckLane(), finiteOr(), mergeIntervals() (+4 more)

### Community 50 - "Transcript Cut Fades"
Cohesion: 0.26
Nodes (13): fadeFilterFor(), round3(), cutSegment(), encodeArgsFor(), escapeConcatPath(), fmt(), isAudioOnly(), probeDuration() (+5 more)

### Community 51 - "Audio File Analysis"
Cohesion: 0.23
Nodes (10): analyze(), clean(), db(), decode(), describe(), frame_rms(), key_estimate(), main() (+2 more)

### Community 52 - "Dev Dependencies"
Cohesion: 0.13
Nodes (15): devDependencies, autoprefixer, eslint, @eslint/js, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, postcss (+7 more)

### Community 53 - "Evaluation Reports"
Cohesion: 0.18
Nodes (13): countAssetFiles(), walk(), escapeHtml(), evalBlock(), generateReport(), outPath, REPO_ROOT, report (+5 more)

### Community 54 - "Music Arrangement"
Cohesion: 0.21
Nodes (7): decode(), default_arc(), fit_grid(), flux(), local_phases(), main(), transient_phase()

### Community 55 - "Locate and Grid Filters"
Cohesion: 0.18
Nodes (5): [cmd, ...rest], font(), gridFilters(), opt, pos

### Community 56 - "Audio Data Extraction"
Cohesion: 0.26
Nodes (5): compute_band_edges(), compute_fft_bands(), decode_audio(), extract(), main()

### Community 57 - "Landing Page Components"
Cohesion: 0.17
Nodes (4): Features, HeroProps, lucide-react, react

### Community 58 - "SFX Tests"
Cohesion: 0.18
Nodes (4): BUNDLED_SFX_DIR, bundledOnly(), record(), run()

### Community 59 - "Licence Classification"
Cohesion: 0.20
Nodes (4): classify(), load_manifests(), rel(), source_name()

### Community 61 - "HyperFrames Config"
Cohesion: 0.20
Nodes (9): authoringSkill, media, autoProxy, paths, assets, blocks, components, registry (+1 more)

### Community 62 - "Basemap Baking"
Cohesion: 0.20
Nodes (5): CENTER, COUNTRIES, framesDir, MARGIN, N

### Community 63 - "Media Record Tests"
Cohesion: 0.27
Nodes (6): recordInManifest(), SFX_SOURCES, noBgm, voicePaths(), writtenAssets(), AGENT_SOURCES

### Community 64 - "Credits Generation"
Cohesion: 0.31
Nodes (5): and_join(), credits(), main(), processing(), say()

### Community 65 - "Speech Pause Map"
Cohesion: 0.33
Nodes (5): stereo_peak(), band_db(), main(), pauses_of(), segments()

### Community 66 - "Index Generation"
Cohesion: 0.39
Nodes (8): formatDims(), formatDur(), generateIndexContent(), pad(), regenerateIndex(), currentRecords(), findByEntity(), indexPath()

### Community 67 - "Band Metrics"
Cohesion: 0.33
Nodes (3): bands(), read_metrics(), window_at()

### Community 68 - "Loudness Input Errors"
Cohesion: 0.40
Nodes (3): need(), InputError, lufs()

### Community 69 - "NPM Scripts"
Cohesion: 0.33
Nodes (6): scripts, build, dev, lint, preview, typecheck

### Community 70 - "Chime Sound Manifest"
Cohesion: 0.40
Nodes (4): chime, description, duration, file

### Community 71 - "App Dependencies"
Cohesion: 0.40
Nodes (5): dependencies, lucide-react, react, react-dom, @supabase/supabase-js

### Community 72 - "Click Sound Manifest"
Cohesion: 0.50
Nodes (4): click, description, duration, file

### Community 73 - "Click-Soft Sound Manifest"
Cohesion: 0.50
Nodes (4): click-soft, description, duration, file

### Community 74 - "Error Sound Manifest"
Cohesion: 0.50
Nodes (4): error, description, duration, file

### Community 75 - "Glitch 1 Manifest"
Cohesion: 0.50
Nodes (4): glitch-1, description, duration, file

### Community 76 - "Glitch 2 Manifest"
Cohesion: 0.50
Nodes (4): glitch-2, description, duration, file

### Community 77 - "Glitch 3 Manifest"
Cohesion: 0.50
Nodes (4): glitch-3, description, duration, file

### Community 78 - "Impact Bass 1 Manifest"
Cohesion: 0.50
Nodes (4): impact-bass-1, description, duration, file

### Community 79 - "Impact Bass 2 Manifest"
Cohesion: 0.50
Nodes (4): impact-bass-2, description, duration, file

### Community 80 - "Key Press Manifest"
Cohesion: 0.50
Nodes (4): key-press, description, duration, file

### Community 81 - "Notification Sound Manifest"
Cohesion: 0.50
Nodes (4): notification, description, duration, file

### Community 82 - "Ping Sound Manifest"
Cohesion: 0.50
Nodes (4): ping, description, duration, file

### Community 83 - "Pop Sound Manifest"
Cohesion: 0.50
Nodes (4): pop, description, duration, file

### Community 84 - "Riser Sound Manifest"
Cohesion: 0.50
Nodes (4): riser, description, duration, file

### Community 85 - "Sparkle Sound Manifest"
Cohesion: 0.50
Nodes (4): sparkle, description, duration, file

### Community 86 - "Typing Sound Manifest"
Cohesion: 0.50
Nodes (4): typing, description, duration, file

### Community 87 - "Whoosh Manifest"
Cohesion: 0.50
Nodes (4): whoosh, description, duration, file

### Community 88 - "Cinematic Whoosh Manifest"
Cohesion: 0.50
Nodes (4): whoosh-cinematic, description, duration, file

### Community 89 - "Short Whoosh Manifest"
Cohesion: 0.50
Nodes (4): whoosh-short, description, duration, file

## Knowledge Gaps
- **7 isolated node(s):** `autoprefixer`, `eslint`, `postcss`, `tailwindcss`, `@types/react` (+2 more)
  These have ≤1 connection - possible missing edges. (Counts symbols only; 771 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `main()` connect `Sound Family Matching` to `Loudness Measurement`, `Cue Folding Config`, `Ambience Bed Generation`, `Tonal Feature Analysis`, `Text and Path Utilities`, `Candidate Contact Sheets`, `Unbake Layer Fitting`, `Review and Packaging`, `Video Moment Finding`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **What connects `autoprefixer`, `eslint`, `postcss` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Film Build Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.052943354313217325 - nodes in this community are weakly interconnected._
- **Why does `measure_loudness()` connect `Loudness Measurement` to `Film Build Tools`, `Sound Family Matching`, `Cue Folding Config`, `Unbake Layer Fitting`, `Style Learning Analysis`, `Reference Style Comparison`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **Should `Plugin CLI Entrypoint` be split into smaller, more focused modules?**
  _Cohesion score 0.06169772256728778 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Cue Folding Config` to `Sound Family Matching`, `Loudness Measurement`, `Ambience Bed Generation`, `Tonal Feature Analysis`, `Text and Path Utilities`, `Candidate Contact Sheets`, `Review and Packaging`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Should `Sound Family Matching` be split into smaller, more focused modules?**
  _Cohesion score 0.045134575569358175 - nodes in this community are weakly interconnected._