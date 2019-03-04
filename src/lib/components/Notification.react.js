import React from 'react';
import PropTypes from 'prop-types';
import {timestampProp} from '../utils';
import {merge} from 'ramda';

export default class DashNotification extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lastMessage: props.body,
            notification: null,
        };
        this.onPermission = this.onPermission.bind(this);
    }

    componentDidMount() {
        const {setProps} = this.props;
        if (!('Notification' in window) && setProps) {
            setProps({permission: 'unsupported'});
        } else if (Notification.permission === 'default') {
            Notification.requestPermission().then(this.onPermission);
        } else {
            this.onPermission(window.Notification.permission);
        }
    }

    componentDidUpdate(prevProps) {
        if (!prevProps.displayed && this.props.displayed) {
            this.sendNotification(this.props.permission);
        }
    }

    sendNotification(permission) {
        const {
            setProps,
            body,
            title,
            icon,
            require_interaction,
            lang,
            badge,
            tag,
            image,
            vibrate,
        } = this.props;
        if (permission === 'granted') {
            const options = {
                requireInteraction: require_interaction,
                body,
                icon,
                lang,
                badge,
                tag,
                image,
                vibrate,
            };
            const notification = new Notification(title, options);
            notification.onclick = () => {
                if (setProps) {
                    setProps(
                        merge(
                            {displayed: false},
                            timestampProp('n_clicks', this.props.n_clicks + 1)
                        )
                    );
                }
            };
            notification.onclose = () => {
                if (setProps) {
                    setProps(
                        merge(
                            {displayed: false},
                            timestampProp('n_closes', this.props.n_closes + 1)
                        )
                    );
                }
            };
        }
    }

    onPermission(permission) {
        const {displayed, setProps} = this.props;
        if (setProps) {
            setProps({permission});
        }
        if (displayed) {
            this.sendNotification(permission);
        }
    }

    render() {
        return null;
    }
}

DashNotification.defaultProps = {
    require_interaction: false,
    n_clicks: 0,
    n_clicks_timestamp: -1,
    n_closes: 0,
    n_closes_timestamp: -1,
};

// Props docs from https://developer.mozilla.org/en-US/docs/Web/API/Notification/Notification
DashNotification.propTypes = {
    id: PropTypes.string,

    /**
     * Permission granted by the user (READONLY)
     */
    permission: PropTypes.oneOf([
        'denied',
        'granted',
        'default',
        'unsupported',
    ]),

    title: PropTypes.string.isRequired,

    /**
     * The notification's language, as specified using a DOMString representing a BCP 47 language tag.
     */
    lang: PropTypes.string,
    /**
     * A DOMString representing the body text of the notification, which will be displayed below the title.
     */
    body: PropTypes.string,
    /**
     * A USVString containing the URL of the image used to represent the notification when there is not enough space to display the notification itself.
     */
    badge: PropTypes.string,

    /**
     * A DOMString representing an identifying tag for the notification.
     */
    tag: PropTypes.string,
    /**
     * A USVString containing the URL of an icon to be displayed in the notification.
     */
    icon: PropTypes.string,
    /**
     *  a USVString containing the URL of an image to be displayed in the notification.
     */
    image: PropTypes.string,
    /**
     * A vibration pattern for the device's vibration hardware to emit when the notification fires.
     */
    vibrate: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
    ]),
    /**
     * Indicates that a notification should remain active until the user clicks or dismisses it, rather than closing automatically. The default value is false.
     */
    require_interaction: PropTypes.bool,

    /**
     *
     */
    displayed: PropTypes.bool,

    n_clicks: PropTypes.number,
    n_clicks_timestamp: PropTypes.number,

    n_closes: PropTypes.number,
    n_closes_timestamp: PropTypes.number,

    setProps: PropTypes.func,
    key: PropTypes.string,
};
