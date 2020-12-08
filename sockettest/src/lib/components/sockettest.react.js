import React, {Component} from 'react';
import PropTypes from 'prop-types';
import * as ds from '../../../socketutil.js';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class sockettest extends Component {
    componentDidMount() {
        ds.DashSocket.connect();
    }

    componentWillUnmount() {
        ds.DashSocket.disconnect();
    }


    render() {
        const {id} = this.props;

        return (
            <div id={id}>
            </div>
        );
    }
}

sockettest.defaultProps = {};

sockettest.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,
};
