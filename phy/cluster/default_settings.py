
# -----------------------------------------------------------------------------
# Spike detection
# -----------------------------------------------------------------------------

def spikedetekt_params(sample_rate):
    assert sample_rate > 0

    return dict(
        # Filter.
        filter_low=500.,
        filter_high=0.95 * .5 * sample_rate,
        filter_butter_order=3,

        # Data chunks.
        chunk_size=int(1. * sample_rate),
        chunk_overlap=int(.015 * sample_rate),

        # Threshold.
        nexcerpts=50,
        excerpt_size=int(1. * sample_rate),
        use_single_threshold=True,
        threshold_strong_std_factor=4.5,
        threshold_weak_std_factor=2.,
        detect_spikes='negative',

        # Connected components.
        connected_component_join_size=int(.00005 * sample_rate),

        # Spike extractions.
        extract_s_before=10,
        extract_s_after=10,
        weight_power=2,

        # Features.
        nfeatures_per_channel=3,
        pca_nwaveforms_max=10000,
    )


# -----------------------------------------------------------------------------
# KlustaKwik
# -----------------------------------------------------------------------------

klustakwik_params = {}


# -----------------------------------------------------------------------------
# Correlograms
# -----------------------------------------------------------------------------

# Number of time samples in a bin.
correlograms_binsize = 20

# Number of bins (odd number).
correlograms_winsize_bins = 2 * 25 + 1

# Maximum number of spikes for the correlograms.
# Use `None` to specify an infinite value.
correlograms_n_spikes_max = 1000000

# Contiguous chunks of spikes for computing the CCGs.
# Use `None` to have a regular (strided) subselection instead of a chunked
# subselection.
correlograms_excerpt_size = 100000


# -----------------------------------------------------------------------------
# Views
# -----------------------------------------------------------------------------

# Maximum number of spikes to display in the waveform view.
waveforms_n_spikes_max = 100

# Load contiguous chunks of waveforms (contiguous I/O is faster).
# Higher value = faster loading of waveforms.
waveforms_excerpt_size = 20

# Maximum number of spikes to display in the feature view.
features_n_spikes_max = 2500

# Load a regular subselection of spikes from the cluster store.
features_excerpt_size = None

# Maximum number of background spikes to display in the feature view.
features_n_spikes_max_bg = features_n_spikes_max

features_grid_n_spikes_max = features_n_spikes_max
features_grid_excerpt_size = features_excerpt_size
features_grid_n_spikes_max_bg = features_n_spikes_max_bg


# -----------------------------------------------------------------------------
# Clustering GUI
# -----------------------------------------------------------------------------

cluster_manual_shortcuts = {
    'reset_gui': 'alt+r',
    'show_shortcuts': 'ctrl+h',
    'save': 'ctrl+s',
    'close': 'ctrl+q',
    # Wizard actions.
    'reset_wizard': 'ctrl+w',
    'next': 'space',
    'previous': 'shift+space',
    'reset_wizard': 'ctrl+alt+space',
    'first': 'home',
    'last': 'end',
    'pin': 'return',
    'unpin': 'backspace',
    # Clustering actions.
    'merge': 'g',
    'split': 'k',
    'undo': 'ctrl+z',
    'redo': ('ctrl+shift+z', 'ctrl+y'),
    'move_best_to_noise': 'alt+n',
    'move_best_to_mua': 'alt+m',
    'move_best_to_good': 'alt+g',
    'move_match_to_noise': 'ctrl+n',
    'move_match_to_mua': 'ctrl+m',
    'move_match_to_good': 'ctrl+g',
    'move_both_to_noise': 'ctrl+alt+n',
    'move_both_to_mua': 'ctrl+alt+m',
    'move_both_to_good': 'ctrl+alt+g',
    # Views.
    'show_view_shortcuts': 'h',
    'toggle_correlogram_normalization': 'n',
    'toggle_waveforms_overlap': 'o',
    'toggle_waveforms_mean': 'm',
    'show_features_time': 't',
}


cluster_manual_config = [
    ('wizard', {'position': 'right'}),
    ('stats', {'position': 'right'}),
    ('features_grid', {'position': 'left'}),
    ('features', {'position': 'left'}),
    ('correlograms', {'position': 'left'}),
    ('waveforms', {'position': 'right'}),
    ('traces', {'position': 'right'}),
]


def on_open(session):
    """You can update the session when a model is opened.

    For example, you can register custom statistics with
    `session.register_statistic`.

    """
    pass


# Whether to ask the user if they want to save when the GUI is closed.
prompt_save_on_exit = True


# -----------------------------------------------------------------------------
# Store settings
# -----------------------------------------------------------------------------

# Number of spikes to load at once from the features_masks array
# during the cluster store generation.
features_masks_chunk_size = 100000


# -----------------------------------------------------------------------------
# Internal settings
# -----------------------------------------------------------------------------

waveforms_scale_factor = .01
features_scale_factor = .01
features_grid_scale_factor = features_scale_factor
traces_scale_factor = .01
