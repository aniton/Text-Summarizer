/**
 * Left part of the website- a place to input text to.
 * @packageDocumentation
 */
import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import { TextField } from '@material-ui/core';

const styles = {
  textInput: {
    width: '40vw',
    height: '80vh',
    margin: '5vh 5vw',
    '& div': {
      width: '100%',
      height: '100%',
      display: 'flex',
      alignItems: 'flex-start',
      '& textarea': {
        lineHeight: '20px',
        fontSize: '16px',
        overflow: 'auto',
        resize: 'none',
      },
      '& fieldset': {
        width: '100%',
        height: '100%',
      },
    },
  },
};

/** Text input form */
function InputForm(props: any) {
  const { classes } = props;
  // Determines textarea max size
  const height = window.screen.height;
  const lineHeight = 20;
  const rows = Math.floor((height * 0.75) / lineHeight);

  return (
    <>
      <TextField
        label="Insert your text here"
        className={classes.textInput}
        variant="outlined"
        multiline
        rowsMax={rows}
      />
    </>
  );
}

InputForm.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(InputForm);
