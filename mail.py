import requests
from vars import *
def send_email(emails, html , text = "",):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox5e9ee65a55034260bde8c61e86f4b04c.mailgun.org/messages",
		auth=("api",mailgunkey),
		data={"from": "horoscrypt@hackodex2022riga.com",
              "Content-Type": "text/html",
			"to": "cemipig.fafasiv@vintomaper.com",
			"subject": "codeX_Horoscrypt meeting notes",
			"text": text,
      "html": html 
            })


def html_preperare(summary, dateTimeEntities, eventEntities):
  html = '''</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody>
</table>

</div>
</div>
</div>


</div>
</div>
</div>



<div class="u-row-container" style="padding: 0px;background-color: transparent">
<div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">



<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>

</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:helvetica,sans-serif;" align="left">
  
<div style="line-height: 140%; text-align: left; word-wrap: break-word;">
<p style="font-size: 14px; line-height: 140%;"><span style="font-family: helvetica, sans-serif; font-size: 16px; line-height: 22.4px;"><span style="font-size: 20px; line-height: 28px;"><strong>SUMMARY</strong></span>:</span></p>
<p style="font-size: 14px; line-height: 140%;"><span style="font-family: helvetica, sans-serif; font-size: 16px; line-height: 22.4px;">{summary} </span></p>
</div>

</td>
</tr>
</tbody>
</table>

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
</tr>
</tbody>
</table>

</td>
</tr>
</tbody>
</table>

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:helvetica,sans-serif;" align="left">
  
<div style="line-height: 140%; text-align: left; word-wrap: break-word;">
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 22px; line-height: 30.8px;"><strong><span style="font-family: helvetica, sans-serif; line-height: 30.8px; font-size: 22px;">Event Dates</span></strong></span></p>
<p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
<ul>
  {eventEntities}
</ul>
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 22px; line-height: 30.8px;"><strong><span style="font-family: helvetica, sans-serif; line-height: 30.8px; font-size: 22px;">To Do List</span></strong></span></p>

<ul>
  {dateTimeEntities}
</ul>
<p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
</div>

</td>
</tr>
</tbody>
</table>

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
</tr>
</tbody>
</table>

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tbody>
<tr>
</tr>
</tbody>

<tr>
<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:helvetica,sans-serif;" align="left">
  
<div align="center">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:helvetica,sans-serif;"><tr><td style="font-family:helvetica,sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:37px; v-text-anchor:middle; width:162px;" arcsize="11%" stroke="f" fillcolor="#000000"><w:anchorlock/><center style="color:#FFFFFF;font-family:helvetica,sans-serif;"><![endif]-->
<a href="" target="_blank" style="box-sizing: border-box;display: inline-block;font-family:helvetica,sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #000000; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
<span style="display:block;padding:10px 20px;line-height:120%;"><span style="font-size: 14px; line-height: 16.8px;">Full recording video</span></span>
</a>
<!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
</div>

</td>
</tr>
</tbody>
</table>

</div>
</div>
</div>


</div>
</div>
</div>



<div class="u-row-container" style="padding: 0px;background-color: transparent">
<div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">



<div class="u-col u-col-50" style="max-width: 320px;min-width: 250px;display: table-cell;vertical-align: top;">
<div style="width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
<!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
</table>

<!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
</div>
</div>


<div class="u-col u-col-50" style="max-width: 320px;min-width: 250px;display: table-cell;vertical-align: top;">
<div style="width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
<div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">

</div>
</div>
</div>


</div>
</div>
</div>



<div class="u-row-container" style="padding: 0px;background-color: transparent">
<div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">



<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
<div style="width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
<div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">

<table style="font-family:helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:helvetica,sans-serif;" align="left">
  
<div style="line-height: 140%; text-align: left; word-wrap: break-word;">
</div>

</td>
</tra
</tbody>
</table>

</div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</body>
      </html>'''
  return html